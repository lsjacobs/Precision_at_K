
def precision(actual, predicted, k):
    act_set = set(actual[:k])
    pred_set = set(predicted[:k])
    result = len(act_set & pred_set) / float(k)
    return result

def sqr(x):
	return x**2

import math


if __name__ == "__main__":
	
	humano=[]
	
#TEXTO 1

	
	#humano.append(["tecnologias","educacao","novas tecnologias","professores","alunos","digital","escola","aula","uso","parte","faz"]) 
	#humano.append(["educacao","alunos","professores","escola","digital","aula","tecnologias","uso","parte","faz","novas tecnologias"]) 
	#humano.append(["educacao","tecnologias","alunos","aula","professores","faz","uso","novas tecnologias","escola","digital","parte"]) 
	#humano.append(["tecnologias","novas tecnologias","digital","educacao","escola","professores","alunos","aula","uso","faz","parte"]) 
	#humano.append(["educacao","novas tecnologias","professores","alunos","digital","tecnologias","escola","faz","uso","aula","parte"]) 
	#humano.append(["novas tecnologias","tecnologias","educacao","digital","escola","professores","uso","aula","parte","alunos","faz"]) 
	#humano.append(["novas tecnologias","educacao","uso","escola","professores","alunos","tecnologias","aula","digital","faz","parte"]) 
	#humano.append(["aula","educacao","tecnologias","escola","professores","alunos","novas tecnologias","digital","uso","parte","faz"]) 
	#humano.append(["educacao","alunos","professores","tecnologias","novas tecnologias","digital","escola","aula","parte","faz","uso"]) 
	#humano.append(["educacao","novas tecnologias","digital","aula","uso","professores","alunos","tecnologias","escola","faz","parte"]) 
	#humano.append(["novas tecnologias","digital","educacao","professores","alunos","tecnologias","escola","aula","parte","faz","uso"]) 
	#humano.append(["novas tecnologias","educacao","digital","tecnologias","escola","professores","alunos","aula","faz","uso","parte"]) 
	#humano.append(["tecnologias","educacao","professores","alunos","escola","aula","novas tecnologias","digital","faz","parte","uso"]) 
	#humano.append(["novas tecnologias","digital","tecnologias","educacao","professores","escola","aula","alunos","uso","faz","parte"]) 
	#humano.append(["educacao","tecnologias","novas tecnologias","escola","alunos","professores","aula","digital","uso","faz","parte"]) 
	#humano.append(["escola","educacao","professores","alunos","aula","novas tecnologias","tecnologias","digital","uso","parte","faz"]) 
	
	# 24 respostas no forms
	
	#algoritmo=["alunos","digital","novas tecnologias","tecnologias","professores","educacao","aula","escola","faz","uso","parte"]
	#sobek=["alunos","digital","educacao","novas tecnologias","parte","aula","escola","faz","professores","tecnologias","uso"]
	
#TEXTO 2
	#humano.append(["sintomas de vicio","jogos","games","videogames","efeitos","negativos","criancas","pesquisa","viciados","azar","familia","estados unidos","alguns"]) 
	#humano.append(["familia","criancas","sintomas de vicio","jogos","videogames","games","pesquisa","viciados","efeitos","negativos","azar","alguns","estados unidos"]) 
	#humano.append(["games","videogames","criancas","sintomas de vicio","viciados","efeitos","jogos","negativos","familia","azar","pesquisa","estados unidos","alguns"]) 
	#humano.append(["criancas","sintomas de vicio","viciados","videogames","jogos","familia","efeitos","negativos","games","azar","pesquisa","estados unidos","alguns"])  
	#humano.append(["jogos","games","videogames","sintomas de vicio","pesquisa","azar","negativos","alguns","familia","efeitos","estados unidos","criancas","viciados"]) 
	#humano.append(["pesquisa","estados unidos","videogames","familia","negativos","sintomas de vicio","criancas","viciados","alguns","efeitos","azar","jogos","games"])
	#humano.append(["viciados","videogames","criancas","pesquisa","familia","games","jogos","negativos","sintomas de vicio","azar","efeitos","estados unidos","alguns"])
	#humano.append(["pesquisa","efeitos","videogames","games","jogos","sintomas de vicio","criancas","familia","viciados","azar","alguns","negativos","estados unidos"])
	#humano.append(["videogames","sintomas de vicio","criancas","familia","efeitos","pesquisa","estados unidos","alguns","jogos","games","azar","negativos","viciados"])
	#humano.append(["games","jogos","negativos","viciados","videogames","alguns","sintomas de vicio","pesquisa","familia","estados unidos","criancas","efeitos","azar"])
	#humano.append(["videogames","games","viciados","sintomas de vicio","criancas","familia","jogos","efeitos","negativos","azar","pesquisa","estados unidos","alguns"])
	#humano.append(["videogames","criancas","sintomas de vicio","pesquisa","estados unidos","familia","games","viciados","efeitos","negativos","jogos","azar","alguns"])
	#humano.append(["videogames","viciados","sintomas de vicio","criancas","pesquisa","estados unidos","efeitos","negativos","games","jogos","azar","familia","alguns"]) 
	#humano.append(["games","videogames","jogos","efeitos","sintomas de vicio","criancas","viciados","negativos","familia","pesquisa","azar","estados unidos","alguns"]) 
	#humano.append(["sintomas de vicio","games","videogames","viciados","negativos","jogos","azar","efeitos","familia","criancas","estados unidos","pesquisa","alguns"])
	#humano.append(["sintomas de vicio","videogames","efeitos","negativos","criancas","jogos","azar","alguns","pesquisa","estados unidos","viciados","games","familia"])
	
	# 20 respostas no forms
	
	#algoritmo=["familia","videogames","sintomas de vicio","viciados","efeitos","alguns","negativos","pesquisa","criancas","estados unidos","jogos","azar","games"]
	#sobek=(["familia","videogames","criancas","jogos","alguns","azar","efeitos","estados unidos","games","negativos","pesquisa","sintomas de vicio","viciados"])
	
#TEXTO 3
	humano.append(["informatica na educacao","educacao","computacao","conhecimento","areas","diferentes","distintas","mundo","vezes","outros","cada","deste"]) 
	humano.append(["educacao","informatica na educacao","areas","conhecimento","computacao","mundo","diferentes","distintas","vezes","deste","outros","cada"]) 
	humano.append(["educacao","informatica na educacao","computacao","conhecimento","diferentes","areas","distintas","deste","mundo","cada","vezes","outros"]) 
	humano.append(["educacao","computacao","informatica na educacao","diferentes","areas","conhecimento","deste","mundo","distintas","cada","vezes","outros"])
	humano.append(["conhecimento","computacao","educacao","informatica na educacao","vezes","outros","cada","mundo","deste","distintas","diferentes","areas"]) 
	humano.append(["informatica na educacao","computacao","educacao","mundo","conhecimento","areas","vezes","diferentes","deste","cada","distintas","outros"])
	humano.append(["informatica na educacao","conhecimento","computacao","educacao","areas","mundo","diferentes","distintas","cada","vezes","deste","outros"]) 
	humano.append(["informatica na educacao","areas","conhecimento","distintas","computacao","educacao","diferentes","cada","vezes","outros","deste","mundo"])
	humano.append(["informatica na educacao","distintas","areas","conhecimento","educacao","computacao","diferentes","vezes","deste","cada","outros","mundo"]) 
	humano.append(["computacao","educacao","conhecimento","vezes","diferentes","mundo","distintas","deste","areas","informatica na educacao","outros","cada"])
	humano.append(["diferentes","distintas","informatica na educacao","areas","conhecimento","educacao","computacao","mundo","vezes","outros","cada","deste"])
	humano.append(["informatica na educacao","educacao","conhecimento","computacao","areas","mundo","diferentes","distintas","outros","vezes","cada","deste"]) 
	humano.append(["informatica na educacao","computacao","educacao","areas","conhecimento","mundo","diferentes","distintas","outros","vezes","deste","cada"]) 
	humano.append(["informatica na educacao","educacao","areas","distintas","computacao","conhecimento","mundo","diferentes","outros","vezes","deste","cada"]) 
	humano.append(["informatica na educacao","computacao","educacao","areas","conhecimento","diferentes","distintas","mundo","deste","outros","vezes","cada"]) 
	humano.append(["informatica na educacao","conhecimento","computacao","areas","educacao","outros","cada","distintas","deste","vezes","diferentes","mundo"])
	
	# 19 respostas no forms
	
	algoritmo=["informatica na educacao","computacao","conhecimento","educacao","vezes","areas","distintas","deste","diferentes","outros","cada","mundo"]
	sobek=(["informatica na educacao","computacao","conhecimento","educacao","outros","areas","cada","deste","diferentes","distintas","mundo","vezes"])
	
#///////

	precision_at=6

	media=0
	variancia=0
	for i in xrange(len(humano)):
		print "humano= "+str(i+1)+": precison@"+str(precision_at)+"= "+str(precision(humano[i],algoritmo,precision_at)) #alterna entre Sobek e Algoritmo
		media=media+precision(humano[i],algoritmo,precision_at)
	
	media=media/len(humano)
	
	for i in xrange(len(humano)):
		variancia=variancia+sqr(precision(humano[i],algoritmo,precision_at)-media)
		
	variancia=variancia/len(humano)
	desvio=math.sqrt(variancia)
	
	print "media: "+str(media) + ", variancia: " + str(variancia) + ", desvio: " +str(desvio)
		