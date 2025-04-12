#Funkce

while True:
	
	def pocitaniUdaju():
		#Ziskavani udaju
		hours = int(input("Zadej pocet hodin: "))
		minutes = int(input("Zadej pocet minut: "))
		seconds = int(input("Zadej pocet sekund: "))

		#Pocitani
		resultSeconds = (hours * 3600) + (minutes * 60) + seconds
		return resultSeconds

	resultSeconds = pocitaniUdaju()

	#Vysledek
	print("Tento cas se rovna", resultSeconds, "sekund.")

