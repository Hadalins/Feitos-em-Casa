import keyword
palavras_reservadas_py = keyword.kwlist
palavras_reservadas_jv = ["abstract","assert","break","case","catch","class","const","continue","default","do","else","enum","extends","final","finally","for","goto","if","implements","import","instanceof","interface","native","new","package","private","protected","public","return","static","strictfp","super","switch","synchronized","this","throw","throws","transient","try","void","volatile","while"]
palavras_reservadas_php = ["and","array","as","break","case","catch","class","const","continue","declare","default","die","do","else","elseif","enddeclare","endfor","endforeach","endif","endswitch","endwhile","extends","for","foreach","function","global","if","include","include_once","instanceof","insteadof","interface","isset","list","new","or","print","require","require_once","return","static","switch","throw","trait","try","unset","use","var","while"]


codigo = input ("digite seu codigo: ")

while True:
  if codigo in palavras_reservadas_py or codigo in palavras_reservadas_jv or codigo in palavras_reservadas_php:
    print (codigo + " - palavra reservada")
    break
  else:
    print ("não existe na lista")
    codigo = input ("digite seu codigo :")