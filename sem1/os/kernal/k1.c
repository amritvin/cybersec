#include<linux/module.h>
#include<linux/kernel.h>
int init_module(void){
	printk(KERN_INFO "%lu\n",read_cr3());
	return 0;
}
void cleanup_module(void){
	printk(KERN_INFO "goodbye\n");	
}
