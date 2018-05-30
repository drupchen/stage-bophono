from bophono import *

bo = ["ཀ་", "ཁ་", "ག་", "ང་",
          "ཅ་", "ཆ་", "ཇ་", "ཉ་",
          "ཏ་", "ཐ་", "ད་", "ན་",
          "པ་", "ཕ་", "བ་", "མ་",
          "ཙ་", "ཚ་", "ཛ་", "ཝ་",
          "ཞ་", "ཟ་", "འ་", "ཡ་",
          "ར་", "ལ་", "ཤ་", "ས་",
          "ཧ་", "ཨ་",
          "ཨི་", "ཨུ་", "ཨེ་", "ཨོ་",
          "རྐ་", "རྒ་", "རྔ་", "རྗ་", "རྙ་", "རྟ་", "རྡ་", "རྣ་", "རྦ་", "རྨ་", "རྩ་", "རྫ་",
          "ལྐ་", "ལྒ་", "ལྔ་", "ལྕ་", "ལྗ་", "ལྟ་", "ལྡ་", "ལྤ་", "ལྦ་", "ལྷ་",
          "སྐ་", "སྒ་", "སྔ་", "སྙ་", "སྟ་", "སྡ་", "སྣ་", "སྤ་", "སྦ་", "སྨ་", "སྩ་",
          "ཀྱ་", "ཁྱ་", "གྱ་", "པྱ་", "ཕྱ་", "བྱ་", "མྱ་",
          "ཀྲ་", "ཁྲ་", "གྲ་", "ཏྲ་", "ཐྲ་", "དྲ་", "པྲ་", "ཕྲ་", "བྲ་", "མྲ་", "སྲ་", "ཧྲ་",
          "ཀླ་", "གླ་", "བླ་", "ཟླ་", "རླ་", "སླ་",
          "རྐྱ་", "རྒྱ་", "རྨྱ་", "སྐྱ་", "སྒྱ་", "སྤྱ་", "སྦྱ་", "སྨྱ་",
          "སྐྲ་", "སྒྲ་", "སྤྲ་", "སྦྲ་", "སྨྲ་",
          "ཀག་", "ཀང་", "ཀད་", "ཀན་", "ཀབ་", "ཀམ་", "ཀའ་", "ཀར་", "ཀལ་", "ཀས་",
          "ལགས་", "གཅོད་", "གཉིས་", "གཏིང་", "གདགས་", "གནོངས་", "གཙབས་", "གཞིགས་", "གཟིགས་", "གཡོར་", "གཤིན་", "གསུངས་", "དཀོན་", "དགག", "དངོས་", "དཔོན་", "དབང་", "དམོད་", "དཀྱིལ་", "དགྱེ་", "དཔྱོད་", "དབྱངས་", "དམྱལ་", "དཀྲིག་", "དགྲ་", "དཔྲལ་", "དབྲོལ་", "བཀག་", "བགགས་", "བཅག་", "བཏག་", "བདག་", "བཙག་", "བཞག་", "བཟའ་", "བཤག་", "བསག་", "བརྐམ་", "བརྒད་", "བརྔད་", "བརྗོད་", "བརྙན་", "བརྟག་", "བརྡ་", "བརྣག་", "བརྩད་", "བརྫང་", "བསྐང་", "བསྒག་", "བསྔགས་", "བསྙག་", "བསྟད་", "བསྡད་", "བསྣན་", "བསྩལ་", "བརྐྱག་", "བགྱང་", "བཀྲ་", "བགྲག་", "བསྲང་", "བཀླག་", "བཟླ་", "བརླ་", "བསླང་", "བརྐྱང་", "བརྒྱ་", "བསྐྱང་", "བསྒྱར་", "བསྐྲད་", "བསྒྲིགས་", "མཁའ་", "མགར་", "མངག་", "མཆན་", "མཇལ་", "མཉམ་", "མཐའ་", "མདང་", "མནག་", "མཚང་", "མཛད་", "མཁྱེན་", "མགྱོགས་", "མཁྲང་", "མགྲིན་", "འཁུར་", "འགག་", "འཆད་", "འཇུག་", "འཐག་", "འདག་", "འཕང་", "འབག་", "འཚོ་", "འཛག་", "འཁྱོག་", "འགྱང་", "འཕྱོ་", "འབྱང་", "འཁྲང་", "འགྲང་", "འདྲ་", "འཕྲག་", "འབྲི་", "འབྲོག་", "ཧྥ་"
        ]

thl_phono = ["ka", "k'a", "ga", "nga",
"cha", "cha", "ja", "nya",
"ta", "t'a", "da", "na",
"pa", "p'a", "ba", "ma",
"tsa", "tsa", "dza", "wa",
"shya", "za", "a", "ya",
"ra", "la", "sha", "sa",
"ha", "a",
"i", "ou", "é", "o",
"ka", "ga", "nga", "ja", "nya", "ta", "da", "na", "ba", "ma", "tsa", "dza",
"ka", "ga", "nga", "cha", "ja", "ta", "da", "pa", "ba", "l'a",
"ka", "ga", "nga", "nya", "ta", "da", "na", "pa", "ba", "ma", "tsa",
"kya", "k'ya", "gya", "cha", "cha", "ja", "nya",
"tra", "t'ra", "dra", "tra", "t'ra", "dra", "tra", "t'ra", "dra", "ma", "sa", "hra",
"la", "la", "la", "da", "la", "la",
"kya", "gya", "nya", "kya", "gya", "cha", "ja", "nya",
"tra", "dra", "tra", "dra", "ma",
"kak", "kang", "ké", "ken", "kab", "kam", "ka", "kar", "kal", "ké",
"lak", "chö", "nyi", "ting", "dak", "nong", "tsab", "shyik", "zik", "yor", "shin", "soung", "kön", "gak", "ngö", "pön", "wang", "mö", "kyil", "gyé", "chö", "yang", "nyal", "trik", "dra", "tral", "rol", "kak", "gak", "chak", "tak", "dak", "tsak", "shyak", "za", "shak", "sak", "kam", "gé", "ngé", "jö", "nyen", "tak", "da", "nak", "tsé", "dzang", "kang", "gak", "ngak", "nyak", "té", "dé", "nen", "tsal", "kyak", "gyang", "tra", "drak", "sang", "lak", "da", "la", "lang", "kyang", "gya", "kyang", "gyar", "tré", "drik", "k'a", "gar", "ngak", "chen", "jal", "nyam", "t'a", "dang", "nak", "tsang", "dzé", "k'yen", "gyok", "t'rang", "drin", "k'our", "gak", "ché", "jouk", "t'ak", "dak", "p'ang", "bak", "tso", "dzak", "k'yok", "gyang", "cho", "jang", "t'rang", "drang", "dra", "t'rak", "dri", "drok", "hp'a"]

wylie = ["ka", "kha", "ga", "nga",
          "ca", "cha", "ja", "nya",
          "ta", "tha", "da", "na",
          "pa", "pha", "ba", "ma",
          "tsa", "tsha", "dza", "wa",
          "zha", "za", "'a", "ya",
          "ra", "la", "sha", "sa",
          "ha", "a",
          "i", "u", "e", "o",
          "rka", "rga", "rnga", "rja", "rnya", "rta", "rda", "rna", "rba", "rma", "rtsa", "rdza",
          "lka", "lga", "lnga", "lca", "lja", "lta", "lda", "lpa", "lba", "lha",
          "ska", "sga", "snga", "snya", "sta", "sda", "sna", "spa", "sba", "sma", "stsa",
          "kya", "khya", "gya", "pya", "phya", "bya", "mya",
          "kra", "khra", "gra", "tra", "thra", "dra", "pra", "phra", "bra", "mra", "sra", "hra",
          "kla", "gla", "bla", "zla", "rla", "sla",
          "rkya", "rgya", "rmya", "skya", "sgya", "spya", "sbya", "smya",
          "skra", "sgra", "spra", "sbra", "smra",
          "kag", "kang", "kad", "kan", "kab", "kam", "ka'", "kar", "kal", "kas",
          "lags", "gcod", "gnyis", "gting", "gdags", "gnongs", "gtsabs", "gzhigs", "gzigs", "g.yor", "gshin", "gsungs", "dkon", "dgag", "dngos", "dpon", "dbang", "dmod", "dkyil", "dgye", "dpyod", "dbyangs", "dmyal", "dkrig", "dgra", "dpral", "dbrol", "bkag", "bgags", "bcag", "btag", "bdag", "btsag", "bzhag", "bza'", "bshag", "bsag", "brkam", "brgad", "brngad", "brjod", "brnyan", "brtag", "brda", "brnag", "brtsad", "brdzang", "bskang", "bsgag", "bsngags", "bsnyag", "bstad", "bsdad", "bsnan", "bstsal", "brkyag", "bgyang", "bkra", "bgrag", "bsrang", "bklag", "bzla", "brla", "bslang", "brkyang", "brgya", "bskyang", "bsgyar", "bskrad", "bsgrigs", "mkha'", "mgar", "mngag", "mchan", "mjal", "mnyam", "mtha'", "mdang", "mnag", "mtshang", "mdzad", "mkhyen", "mgyogs", "mkhrang", "mgrin", "'khur", "'gag", "'chad", "'jug", "'thag", "'dag", "'phang", "'bag", "'tsho", "'dzag", "'khyog", "'gyang", "'phyo", "'byang", "'khrang", "'grang", "'dra", "'phrag", "'bri", "'brog", "h+pha"]

options = {
  'aspirateLowTones': True,
  'prefixStrategy': 'always'
}


converter = UnicodeToApi(options=options) # try with CAT for Amdokä

API = [converter.get_api(syl) for syl in bo]

for tib, ortho, phono, api in zip(bo, wylie, thl_phono, API):
    print('{},{},{},{}'.format(tib, ortho, phono, api))
