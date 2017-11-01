def permutations_sorted( list_chars ):
  if len(list_chars) == 1:  # only one permutation for a 1-character string     
    yield list_chars
  elif len(list_chars) > 1:
    list_chars.sort()
    for i in range(len(list_chars)):
      # use each character as first position (i=index)                          
      head_char = None
      tail_list = []
      for j,c in enumerate(list_chars):
        if i==j:
          head_char = c
        else:
          tail_list.append(c)
      # recursive call, find all permutations of remaining                      
      for tail_perm in permutations_sorted(tail_list):
        yield [ head_char ] + tail_perm

def puzzle( s ):
  print "puzzle %s" % s
  results = []
  for i,p_list in enumerate(permutations_sorted(list(s))):
    p_str = "".join(p_list)
    if p_str == s:
      results.append( i+1 )
  print "string %s was seen at position%s %s" % (
    s,
    "s" if len(results) > 1 else "",
    ",".join(["%d" % i for i in results])
  )
  print ""


if __name__ == '__main__':
  puzzle("aumsrikalima")  
