#include<linux/module.h>
#include<linux/kernel.h>
#include<linux/proc_fs.h>
#include<asm/uaccess.h>
#define PROCFS_MAX_SIZE 1024
#define procfs_name "myfile_proc"
#define DRIVER_AUTHOR "amritvin.org"
#define DRIVER_DESC "My licensed driver @amritvin.org"
static long procfs_buffer_size = 0;
static char procfs_buffer[PROCFS_MAX_SIZE];

struct proc_dir_entry *Our_Proc_File;

static ssize_t procfile_read(struct file *file, char *buffer, size_t length, loff_t *offset)
 {

    static int finished = 0;
    if (finished) {
        printk(KERN_ALERT "Fully read");
        finished = 0;
        return 0;
    }
    finished = 1;
    if (copy_to_user(buffer, procfs_buffer, procfs_buffer_size)) {
        printk(KERN_ALERT "Nothing saved in the file");
        return -EFAULT;
    }
    return procfs_buffer_size;
}

static ssize_t procfile_write(struct file *file, const char *buffer, size_t len, loff_t *off)
{

    if (len > PROCFS_MAX_SIZE)
	   procfs_buffer_size = PROCFS_MAX_SIZE;
    else
	   procfs_buffer_size = len;
     if(copy_from_user(procfs_buffer,buffer,procfs_buffer_size))
	return -EFAULT;
     printk(KERN_DEBUG "procfs_write:write %lu bytes\n",procfs_buffer_size);
     return procfs_buffer_size;
    }



static struct file_operations hello_fops = {
    .owner = THIS_MODULE,
    .read = procfile_read,
    .write = procfile_write,
};

int init_module()
 {
    Our_Proc_File=proc_create(procfs_name, 0777, NULL,&hello_fops);
     if(Our_Proc_File == NULL) {
        remove_proc_entry(procfs_name,NULL);
        printk(KERN_ALERT "Error : could not intialize /proc/%s\n",procfs_name);
        return -ENOMEM;
    }

    printk(KERN_INFO "/proc/%s created\n",procfs_name);
    return 0;
}

void cleanup_module () {
    remove_proc_entry(procfs_name,NULL);
    printk(KERN_INFO "/proc/%s removed \n",procfs_name);

}


MODULE_LICENSE("GPL");
MODULE_AUTHOR(DRIVER_DESC);
MODULE_DESCRIPTION(DRIVER_DESC);
