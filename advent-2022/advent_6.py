ex1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# dup at 1 & 3, start checking from 2. 
# 1 - 4
# 2 - 5
# first num that's bigger than first num but less than second num
ex2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# dup at 0 and 3, start checking at 1
# 0 - 3
# 1 - 4
ex3 = "nppdvjthqldpwncqszvftbrmjlhg"
# dup at 1,2. start checking at 2
# 1 - 4
# 2 - 5
ex4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# dup at 0, 2. start checking at 1
# 0 - 3
# 1 - 
ex5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# dup at 0, 3. check at 1. dup at 2 & 4, check at 3
actual = "grvrnvrnnjljbjqjpqjjvhhzwwrbwwbblrltrrpbbbbqnnqbbbbsvbvmbvmbbrsrqrzrllwbbbqzqrqnqrnrjnnjccdggwqqhrrjcjmjmllgrlglhlclmlvlvsshwwsggmfmdfddgdfftrrczrcczhzppgdgrdggghmmdwwqgggslglfgfcgccmjcjwjrwjrjcrjjsgjjvddpwpgpbbgwbgwwhnhfftbffhpfphhfqfrqfrfnfpprvrsrhrfrllfhhrsrhssvfsvsnvsnsswtwtlthllrjjwddtggzczgcchwcwppfbbdvdrdzrdrvrwwsbsfbssqfsfjsjcscttlztllgjjlbbdsdtssvvvwlvlqqnhqqtdqtddjcdcjjpbphhgtgtqtzqqzhqqtgtvtmvtvrvqrvvfmfmppzzbwwnddzttfpfrrlddbppfqppnwnswwdhwdwjjqljqqthtnhnddgmgcmgcmgcmmfmfttrzzfdzztllmjlllgcgbbcqcvccpnndbdjbjmmzbztzptzpprpddptpprhhvlvmlmpmmljjnnjsjfjjvgjjvzzfgfzfbftbftttgstgstgtpggflfcfqqtctltgltldlzdlzzmmlddnvddzfddppmnpptzptpvttwstwswvwrvvbfbjjjbmjjdvdvrvdddrwrhrzrqqhghhrwhwhrrmppsgpsgszzdfdfwwmtwtvwvgvffmqqqtqntqnnjcncbnbwnnzggrdrqqjbqjjwjqqqwlqwlwzlljhhfsfsqsrqqhwqqwbbqbvvlflrrlglbbjhhjmhjjcmcjcgczcfcgcqqczcnnvjnnlddmpmcppgvgjgddvrrnsnmnqmqgmmnppwgwcgwgssbddgtdgdgmdgmgvvmjmvmjmvvsfssdgdghdggbfbqbdbjbsbmmrpmrprggbllwrwpwtppzvppzsssdnsdnnvnhvvvzvfzfqqnnmlnltldtdvdbdblddsmmlccmlmvlmvmmcsctctrtsrstsbsrshsddlmddmppgsscttnrtrqqcvcwwlnlznnnvcnvvtnvnbnmbmvmppjgjdjtddmpdmdvvmgvvdqdlqlhhzccsggjdjsdsttctjctjtfjttppdzpzzbjbwwmwbblslzslzszlzrrcbrrfggvcczjjtbbdnnggbwblwlbwlwqqfvfqfddrrfccvlllhmhhhrthrthrrnbnzbbpzplphprrrnbbghhnshnhbblqqqvwwffnmnmhhtccpqpvqvbvnvvfnfsnffdjdllwffcddgcgrgjrggchcpcddtbbdtdmtdmmhhtphtpppclcpcvcjvcjjfqfzqqphpnhnrnhhpdhhtfhhbbmqmfmsmvssgqqfssqgglnnqmnmbnmbbllrdrgdrdvrdvdsvvnddgtgddcdqdsqdqbqqlhhwdhdgdcgcdchchrchhpvvpgvgrrfggwfwgmpddbhfngtrwswfszgsggnpsntjpslrpjqsffzrlnbnzdtqpqtjzwlhhgrsrbvnccnsjmzcbqgcbtbqlzhnpnhhrrvqwjwzzvrlcrmjhcscrqhpqmfzbnvcwwqhcjjlnggmpbwztzfswmsbjshnsgfmdlzvzczhrdwgwbghszpnbfpctrshbfhspsczcqcrrqcpwwpfzhjqtpqgjbztrpzrlgfdjbmlwdvlvnfmdzbwsbbhlbszvwcpztlchjrqbmsftltmqpfgdpmdgjvwqqtjsqlfqrwmsnlqgsbqfwsdnfvzthmbplvszfcmlptlcjpnfpjsphsmmjplwjqphgvzbtbjtpttqhlwtgnrjvmvsfsztmsqszzlhqqhfslsvhzgtsssfctzgsqbgdzlpwbsmpcnjqshhhcwqdsdzdhnjfqzqnqdlrpddcgrgldgqbjmdtwgppdczzrjvmcfqjbpjzbtjmgdphlbwnsnpfdqlhwvvmpwzsrztnwvtlbphljmjwsgbphgmwhdmfhpvsmvsjccjhfvqtvfmmlnggncltvtrgmbtfqsvfnlvcmjnjwzcrpjnsgntvhjbtdlptshbhhchqmsprhqzdnfpjqccdfvnzjtlbsmmwvzlwlvmsbrnhqctvtvbfhntdctjnrbcrrlmsnwbbjbcbbgrrhfqwzwwfgvsvgbwnttghtgpspzwzfhffsqjvwwttntnvlwftsfvtttgnprzrzsghvjrdtsfdvzswhmrfcdqsgvrlhzbnvbmjlqrftnnbtwqtvlvwznfbslhdqjbntdgpprfqchjvgvzjssdztjlzwfljjmfvzrbbtczggzqwrnqqgzzcbqjcpfqfrbwtdjrrvbszsjdjcpdfjscsvnltcgwvqsgnhbfgnfnddnpmbzbptrmvqzpvbdpfdvtlmgnnjwflgdbfnmvsdnmlvgcpwflwvdbtbfwtfpsmqsplnzwlwgvbjrhghwrnrswsggbqpdjcjrgbgnsqdvwzzwftvjqgjzzcdvpbbjzpphmbcqmrjvgqwfgrsnqvhwflmhgrlvbpwdcsrlqwfrwppqbrdhwqtvczpclpsbsjcptgblbbsqmbhjjgzwvlcnhnzcttmpjsgchmppgphqlzlcsqcgbbjgtjjvmttdztfdptzgvmpnqrcmpmcdlpnbztllvqbggqbqhlqvdwsrwzsjwfrqvcbvsgfdptmrzpvdfblmhlzrvpmsljlqqzrhlnmwncpfhvqlsbtrjbfcrnfvjvddrhdbbczjdsrdvzlbqrccssdzcpmdsqbprjppfzdwfdswptgzcmjqfhcwsqfqhvrslffqfbcvhdzljzrmtwmfdwzdhhjcmbjtvjhzzwfqhrcslztdbnlwmmhbbbgdscjcdzftnchqfnflnsdqjscfrqpnfbftpzvtmrwncqfqqflschpfnjsjlqcjdjgtwpqhgcnjdmnnvmmpwdspmnrgqrptqwcvbtdwpqlbtwpqgwgfrzlrhtvrvzhmhmwhfdsrhpcczqfltsgtgrfwcvlcvtlhqqwnrqgzpnzbfmzbdwqwbsfvbshrgzqdbgvrhzhzlbqsfzttmsnmrqmwgtzbvdqdrbgcpclzjrhdbjtpcdbbznjgtbwbqrnpvffdmwtrbhhstcmnjcwbbnmpbvmjprtzgcptmtrffwhvfgdljnrbbrblbfbgdwtjrtgqgrpvpgjqrjzczvvlspgdbzftqgqvgdqlglbgvgjdcztznszcwfqhmwbrbjcfstzdcmdsssqfhtzpdgmzjscvbdzgbhhgdqgvfwrzmhdrhlsvlzjjzbzdljcbhncppwrtptjgszlqsrqpzqcsgvdvzmgvwgsncnbffttslphcstqvfwbwzbflmshcbnhpljgqwmmwwzlgpbcqnrtqlwcjcrclfdrnnmvtbfdztdfvtqrsgdptfcfpzpsldhzmrngggfvdqggtlfqqwsldprcffsstnnpmsbbvghdbpprqbssnprdbqclzqtgsrczwcvqwrrfmmfwsndvtvqljwwglrgbphdvvwgctbbmtrbpzqtspgrlhmnhjcdwhwvssgspzjbcfjttjqbdpdmptfzzjcfqljpqddfssmffqprvbptfvdshsdmfmdtmlbnmbmjjjsgmlmwmgcwhbrbgchrstptvdlqgddfzddlzhwjmsvvcjwvqtzjtsctfmzchlbrvlgdzbvdlbfpvhptpltrdmcgjghcpwvwqqnrzdtnmgdncplhdpsgpnbprbgshffwwsdhpgqsbmwdtpnhhltlcqfrjtswcchzvlhdgrmjwhgwppdjqlgmdhwbllqvzrchgclmqdlghjsvmwlflmhhmdzbfjhjnvwphnjbclmdpgflqgtfsmsjslntfcmtbphnrgpdcqtjzjttdtgjmvhzsrfnrjqssvwpcslpfstbpfsrsntmftmdgsqrrsnddqfmchrhtlhmqndvvllnvltdzfphjqnvmcdsgfpcmjftgdpntjzplqljhtthvnbzbzwvfnqsjvnfwhmtbsspjslgfjvdgfjpwrsgqwntntjcqtdgnhnsfwhhqfwbwhdrftj"

def calc_when_first_diff(input_str):
	idx = 0
	final = 0
	num = 4
	while idx < len(input_str):
		print(idx)
		seen = []
		seen_idx = {}
		first = 0
		last = 0
		for x in range(idx, idx + num):
			# print("x is " + str(x))
			curr_letter = input_str[x]
			if curr_letter in seen:
				# print("breaking in for")
				first = seen_idx[curr_letter]
				last = x
				break
			else:
				seen.append(curr_letter)
				seen_idx[curr_letter] = x
		if len(seen) == num:
			# print("breaking in while")
			break

		# four_set = set(list(input_str[idx:idx+num]))
		# if len(four_set) == num:
		# 	final = idx + num
		# 	break
		# idx += 1
		# print("last is " + str(last))
		# print("first is " + str(first))
		idx = first + 1
	final = idx + num

	return final

# print(calc_when_first_diff(ex1))
# print(calc_when_first_diff(ex2))
# print(calc_when_first_diff(ex3))
# print(calc_when_first_diff(ex4))
# print(calc_when_first_diff(ex5))
print(calc_when_first_diff(actual))