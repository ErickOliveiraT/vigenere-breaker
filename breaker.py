language = 'english'
#language = 'portuguese'

#Delete spaces from a encoded input
def delete_spaces(string):
	output = ''
	for char in string:
		if char != ' ':
			output += char
	return output

#Build comparations table
def build_table(string):
	arq = open('data.dat', 'w')
	arq.write(string+'\n')
	for i in range(1,len(string)):
		line = '*' * i
		line += string
		for i in range(0,len(line)):
			if i < len(string):
				arq.write(line[i])
			else:
				arq.write('\n')
				break
	arq.close()

#Get amount of lines from data.dat
def getLineAmount():
	arq = open('data.dat', 'r')
	lines = 0
	for line in arq:
		lines += 1
	arq.close()
	return lines

#Get amount of lines from data2.dat
def getLineAmount2():
	arq = open('data2.dat', 'r')
	lines = 0
	for line in arq:
		lines += 1
	arq.close()
	return lines

#Get a line from data.dat
def getLine(line_number):
	arq = open('data.dat', 'r')
	_id = 0
	for lines in arq:
		_id += 1
		if _id == line_number:
			arq.close()
			return str(lines)

#Get a line from data2.dat
def getLine2(line_number):
	arq = open('data2.dat', 'r')
	_id = 0
	for lines in arq:
		_id += 1
		if _id == line_number:
			arq.close()
			return str(lines)

#Find coincidences between a line and the first one
def compare(line):
	first = getLine(1)
	matches = 0
	for j in range(0,len(line)-1):
		if first[j] == line[j]:
			matches += 1
	return matches

#build coincidences vector
def build_vector():
	linesAmount = getLineAmount()
	coincidences_vector = []
	for i in range(2,linesAmount+1):
		coincidences_vector.append(compare(getLine(i)))
	return coincidences_vector

#build blocks for function separate()
def build_block(start, distance, string):
	vector = []
	vector.append(start)
	aux = start+distance
	while aux < len(string):
		vector.append(aux)
		aux += distance
	block = ''
	for pos in vector:
		block += string[pos]
	return block

#break the text in blocks of length letters
def separate(string, length):
	arq = open('data2.dat', 'w')
	for i in range(0,length):
		row = build_block(i, length, string)
		arq.write(row+'\n')
	arq.close()

#find position of the greatest number in a vector
def find_greatest(vector):
	maxi = 0
	pos = -1
	max_pos = 0
	for number in vector:
		pos += 1
		if number > maxi:
			maxi = number
			max_pos = pos
	return max_pos

#calculates frequency of letters in the blocks
def calculate_frequency():
	pos = 'abcdefghijklmnopqrstuvwxyz'
	modas = []
	for line in range(0,getLineAmount2()):
		freq = []
		row = getLine2(line+1)
		for char in pos:
			cont = 0
			for letter in row:
				if letter == char:
					cont += 1
			freq.append(cont)
		modas.append(pos[find_greatest(freq)])
	return modas

#turn a vector into a string
def filter_key(vector):
	key = ''
	for char in vector:
		key += char
	return key

#estimate key by the frequency analysis
def estimate_key(vector):
	pos = 'abcdefghijklmnopqrstuvwxyz'
	if language == 'english': 
		prime = 'e'
	elif language == 'portuguese':
		prime = 'a'
	prime_index = pos.find(prime)
	pre_key = []
	key = []
	for index in vector:
		distance = pos.find(index)-prime_index
		if distance < 0:
			distance *= -1
		pre_key.append(distance)
	for number in pre_key:
		key.append(pos[number-1])
	return filter_key(key)

def breakText(encoded):
	encoded = encoded.lower()
	encoded = delete_spaces(encoded)
	build_table(encoded)
	vector = build_vector()
	print(vector)
	length = int(input('Key length estimative: '))
	separate(encoded, length)
	modas = calculate_frequency()
	key = estimate_key(modas)
	print('Estimated key = {}'.format(key))












breakText('tie vnjtfd ttbtfs pf bmfrjcb uta donmpnmy lnpwo at tie vnjtfd ttbtfs vs pr vs pr bmfrjcb it a dovnurz cpmqotee og suauet a geeesam djsurjcu fjvf mbjpr temfhowesnjnh tfrsiuosifs bne vbrjovs qotsfstipnt au mjlmipn tqvase nimet mjlmipn lm uhf uoiuee suauet it tie xosles uhjre os fpusti lbrhett dovnurz bz tptbl brfa bne it smihhulz snamlfr uhbn uhf eotjrf cpnuioeot pf fusoqet mjlmipn tqvase nimet mjlmipn lm xiuh b pppvlbtjoo og owes mjlmipn qeppme uhf ut it tie uhjre mpsu pppvlput cpuotsy uhf cbpjtbl js xathjnhtpn ec bne tie masgfsu cjtz bz pppvlbtjoo it nfw zosk diuy gostzejgit ttbtfs bne tie daqiuams geeesam djsurjcu ase dootjgvovs jn oosti anesida ceuwfeo cbnbdb aod neyido uhf suaue pf blbsla js jn uhf npruhxett dosnfr pf oosti anesida cosdfrfd cy daoaea uo uhf ebsu aod bcsots uhf bfrjnh surbiu fson rvstib tp tie xett uhf suaue pf iaxaji js bn brdhjpflbgp io tie nie-pbcjfjc pcfao tie vs uesrjtprjet ase tcbtuesee acovt uhf pbcjfjc pcfao aod uhf cbrjbcebn teb surftdhjnh adrpst njnf ogfjcjam tjmf zpnfs uhf eytsenemy eiwessf gfohrbpiy dljmbtf aod ximdmige pf uhf uoiuee suauet mbkf iu ooe pf uhf wprmdt mfgbdjvfrte dovnurjet')

#gigante = sdcisgeerz ahit ud ucaerp tvleo goca jscvzf oe vlpmgzz prfl o gfzgioxa hip el sdtfi pstfpvvboo hip tva z osxptzjz dv efesflr r qtfio oe mwreesce jsx srppr r gpnyo
#do video = vvhqwvvrmhusgjg
#encoded = tftsmoz ph ix egaofee sdtflnvz
#plain = Futebol eh um esporte estranho
#pass = ola
#grande ingles = hse lbttvr dtrhps ft lmvftcr ida tcxmfbwy bbzwe od tys fnzhpd jhltvg fs ff fs ff lmvftcr wd a tcfnkfj cfaaojso ow geaksd a wsoeiow dzgerzqe fzjp mrxzr jswfxcgeibtnx hpriweoiwps rbo vrftolg aojgpsjwznj oe mzzwifb dqloce dwwej atlcwzn ba ehv iyikso skoeej wd tys hoizos kvtru cc fficty zlrxsdt tcfnkfj bp hztrz lrvo lnu wd scwrhkzj sdowlvf ehrb ehv sytzfp cfbeiesyt ft puicaej atlcwzn jefais xicsd mzzwifb vm nweh r dzplzltzcy ow cgei atlcwzn gszpcs ehv id ij hse kvtru azsk dzplzzuj qzuehcy kvp crdttrz ts nodhzbrtfb oc rbo tys waiupsk qttp pj pfdflrhtoe wd nvk joiy nikm qoihjezust jhltvg lnu hse toaikows wsoeiow dzgerzqe ais noehtglcfs zb yoihs adscito mekkpee qlnrrl aer xeowno kvp skoee ft llrgva zg tn kvp nffehnsdt tccnvf zf eccty oxeiwna sccdvfpd sm naeooa kc ehv slsk oyd rqcojg ehv pprzbr skflik tcod ffsjwl tf hse nsdt kvp skoee ft sanoti zg ln rfnhzdplruz ie hse dwo-prqtfzq zcvoy tys fs kscrzhzrzsd ais dcrheeiso ascft kvp prqtfzq zcvoy aer ehv qlrzpmerb der gervhnhzbr atfzsj btnv cqfzqtac htmv nznvg ehv sitisxecm oimscsv upoxflpym nlzaltv oyd nwwdcwqe ft ehv iyikso skoeej alkv we oes zf kvp wffwdj apgrrtvvfde tcfnkftej