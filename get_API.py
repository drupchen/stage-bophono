from bophono import *

dictee = ["ཀ་", "ཁ་", "ག་", "ང་",
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

options = {
  'aspirateLowTones': True,
  'prefixStrategy': 'always'
}


converter = UnicodeToApi(schema="CAT", options = options) # try with CAT for Amdokä

for syl in dictee:
    print(converter.get_api(syl))
