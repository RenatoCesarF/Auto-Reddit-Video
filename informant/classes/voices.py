from enum import Enum


class Voice(Enum):
    def __str__(self):
        return str(self.value)
 
    #DISNEY VOICES
    EN_US_GHOSTFACE =   "en_us_ghostface"            # Ghost Face
    EN_US_CHEWBACCA=    "en_us_chewbacca"            # Chewbacca
    EN_US_C3PO=         "en_us_c3po"                 # C3PO
    EN_US_STITCH=       "en_us_stitch"               # Stitch
    EN_US_STORMTROOPER= "en_us_stormtrooper"         # Stormtrooper
    EN_US_ROCKET=       "en_us_rocket"   

    #ENGLISH VOICES
    EN_AU_001 = "en_au_001"                  # English AU - Female
    EN_AU_002 = "en_au_002"                  # English AU - Male
    EN_UK_001 = "en_uk_001"                  # English UK - Male 1
    EN_UK_003 = "en_uk_003"                  # English UK - Male 2
    
    EN_US_001 = "en_us_001"                  # English US - Female (Int. 1)
    EN_US_002 = "en_us_002"                  # English US - Female (Int. 2) #boa
    EN_US_006 = "en_us_006"                  # English US - Male 1 # boa
    EN_US_007 = "en_us_007"                  # English US - Male 2
    EN_US_009 = "en_us_009"                  # English US - Male 3
    EN_US_010 = "en_us_010"                  # English US - Male 4

    #EUROPE VOICES 
    FR_001= "fr_001"                         # French - Male 1
    FR_002= "fr_002"                         # French - Male 2
    DE_001= "de_001"                         # German - Female
    DE_002= "de_002"                         # German - Male
    ES_002= "es_002"                         # Spanish - Male
  
    #AMERICA VOICE S 
    ES_MX_002= "es_mx_002"                  # Spanish MX - Male
    BR_001=    "br_001"                     # Portuguese BR - Female 1
    BR_003=    "br_003"                     # Portuguese BR - Female 2
    BR_004=    "br_004"                     # Portuguese BR - Female 3
    BR_005=    "br_005"                     # Portuguese BR - Male
  
    #NARRATOR  
    EN_MALE_NARRATION = "en_male_narration"
      
