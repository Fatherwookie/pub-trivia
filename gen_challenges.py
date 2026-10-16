import json

with open('/home/claude/pub-trivia/questions.json') as f:
    questions = json.load(f)

challenges = [
    # Q0: pound cake ingredients
    ("How many total ingredients are in the original pound cake recipe?", "4 (butter, sugar, flour, eggs)"),
    ("What classic cake takes its name from the equal weight of each of its main ingredients?", "Pound cake"),
    # Q1: Dizzy Gillespie trumpet
    ("What was Dizzy Gillespie's real first name?", "John (John Birks Gillespie)"),
    ("What style of jazz did Dizzy Gillespie help pioneer?", "Bebop"),
    # Q2: Lucky Charms hearts pink
    ("What company makes Lucky Charms cereal?", "General Mills"),
    ("What marshmallow shape in Lucky Charms is blue?", "Diamond"),
    # Q3: Levi's two horses
    ("In what year were Levi's blue jeans first patented?", "1873"),
    ("What material are Levi's jeans primarily made of?", "Denim"),
    # Q4: Tour de France yellow jersey
    ("What color jersey does the best climber wear in the Tour de France?", "Polka dot (white with red dots)"),
    ("What color jersey does the points leader wear in the Tour de France?", "Green"),
    # Q5: Hawaii 8 islands
    ("What is the largest Hawaiian island by area?", "Hawaii (the Big Island)"),
    ("In what year did Hawaii become a US state?", "1959"),
    # Q6: 9-ball striped balls
    ("In 9-ball pool, what numbered ball must be pocketed to win?", "9"),
    ("In 9-ball pool, how many total balls are used?", "9"),
    # Q7: Marine One
    ("What is the call sign of the US President's official aircraft?", "Air Force One"),
    ("What US military branch provides the Presidential helicopter?", "Marines"),
    # Q8: Obama 44th president
    ("Who was the 43rd US President?", "George W. Bush"),
    ("In what year did Barack Obama first take office?", "2009"),
    # Q9: Motorola first handheld phone
    ("Who made the first handheld mobile phone call in 1973?", "Martin Cooper"),
    ("In what city was the first handheld mobile phone call made in 1973?", "New York City"),
    # Q10: Hemisphere 10 letters
    ("What prefix means 'half' in scientific terms?", "Hemi"),
    ("What is the proper term for the half of Earth north of the equator?", "Northern Hemisphere"),
    # Q11: Vanderbilt in Nashville
    ("What are Vanderbilt University's sports teams called?", "Commodores"),
    ("What famous family endowed the university in Nashville bearing their name?", "Vanderbilt (Cornelius Vanderbilt)"),
    # Q12: Heptad = 7
    ("What is the proper term for a group of 8 things?", "Octad"),
    ("What is the Greek prefix for the number 7?", "Hepta"),
    # Q13: Cricket ears on legs
    ("What part of a cricket produces its chirping sound?", "Wings (forewings)"),
    ("How do male crickets produce their characteristic chirping sound?", "Rubbing their wings together (stridulation)"),
    # Q14: Baccarat 2 cards
    ("What is the highest possible hand value in Baccarat?", "9"),
    ("In Baccarat, whose hand value must you bet on to win — player or banker?", "Either (you bet on player, banker, or tie)"),
    # Q15: Helio = Sun
    ("What is the scientific name for the study of the Sun?", "Heliophysics"),
    ("What is the prefix 'geo' related to?", "Earth"),
    # Q16: Vermillion = red
    ("What mineral is vermillion paint traditionally made from?", "Cinnabar (mercury sulfide)"),
    ("What two primary colors mix to create vermillion's general family of hue?", "Red and orange"),
    # Q17: Thursday = Thor's day
    ("What day of the week is named after the Norse goddess Frigg?", "Friday"),
    ("What day of the week is named after the Roman god Saturn?", "Saturday"),
    # Q18: Hepatic = liver
    ("What is the medical term for inflammation of the liver?", "Hepatitis"),
    ("What prefix refers to the kidney in medical terms?", "Nephro (or renal)"),
    # Q19: Largest N. American mammal = bison
    ("What is the national mammal of the United States?", "American bison"),
    ("In what US national park can wild bison reliably be found today?", "Yellowstone"),
    # Q20: Braille 6 dots
    ("Who invented the Braille reading system?", "Louis Braille"),
    ("How many different Braille characters can be made from 6 dots?", "64"),
    # Q21: Malachite = green
    ("What metal gives malachite its distinctive green color?", "Copper"),
    ("Malachite is a carbonate mineral of what metal?", "Copper"),
    # Q22: Lepus = hares
    ("What constellation in the night sky represents the hare?", "Lepus"),
    ("What is the primary difference between a hare and a rabbit?", "Hares are larger with longer ears and are born with fur and open eyes"),
    # Q23: Target logo 1 red ring
    ("What is Target Corporation's stock ticker symbol?", "TGT"),
    ("What color is the outer circle in the Target logo?", "Red"),
    # Q24: Caber tossing
    ("In what country did the Highland Games originate?", "Scotland"),
    ("In caber tossing, what position is considered a perfect toss?", "12 o'clock (caber pointing straight away)"),
    # Q25: Cosmonaut
    ("Who was the first human in space?", "Yuri Gagarin"),
    ("What is the Chinese equivalent term for astronaut?", "Taikonaut"),
    # Q26: Tercentenary = 300 years
    ("What term describes a 100-year anniversary?", "Centenary or centennial"),
    ("What term refers to a 500-year anniversary?", "Quincentenary"),
    # Q27: GHW Bush last VP elected president
    ("Which president did George H.W. Bush serve as Vice President under?", "Ronald Reagan"),
    ("Before George H.W. Bush, who was the last sitting VP to be elected president?", "Martin Van Buren (1836)"),
    # Q28: Mandarin more spoken than Cantonese
    ("How many native Mandarin speakers are there approximately?", "About 900 million"),
    ("What language family does both Mandarin and Cantonese belong to?", "Sino-Tibetan"),
    # Q29: Ant venom = formic acid
    ("From what Latin word for ant does formic acid get its name?", "Formica"),
    ("What is the chemical formula for formic acid?", "HCOOH"),
    # Q30: Diastema = gap in teeth
    ("Which famous model is well known for her prominent diastema?", "Lauren Hutton"),
    ("What is the medical term for the condition of having naturally missing teeth?", "Hypodontia"),
    # Q31: Dipsomaniac = alcohol
    ("What is the clinical term for a compulsive craving for alcohol?", "Dipsomania"),
    ("What medical condition is characterized by an uncontrollable urge to drink alcohol?", "Alcohol use disorder"),
    # Q32: Orzo = pasta
    ("What shape does orzo pasta resemble?", "Rice grains"),
    ("From what language does the word 'orzo' come, meaning 'barley'?", "Italian"),
    # Q33: Mojito meaning
    ("In what country did the Mojito cocktail originate?", "Cuba"),
    ("What are the main ingredients in a classic Mojito?", "White rum, lime juice, sugar, mint, soda water"),
    # Q34: Mach = sound
    ("What is the approximate speed of sound at sea level?", "About 767 mph or 1,235 km/h"),
    ("What does 'Mach 2' mean in terms of speed?", "Twice the speed of sound"),
    # Q35: PDF P = Portable
    ("What company created the PDF format?", "Adobe"),
    ("What does the 'F' in PDF stand for?", "Format"),
    # Q36: UFC round = 5 minutes
    ("How many rounds are in a non-title UFC bout?", "3"),
    ("How long is the rest period between UFC rounds?", "1 minute"),
    # Q37: Flea = bubonic plague
    ("What rodent was the primary carrier of plague-infected fleas during the Black Death?", "Black rat"),
    ("Approximately what percentage of Europe's population died in the Black Death?", "One-third to one-half (30-60%)"),
    # Q38: Galileo in Bohemian Rhapsody
    ("What band recorded Bohemian Rhapsody?", "Queen"),
    ("In what year was Bohemian Rhapsody originally released?", "1975"),
    # Q39: Pillywink tortures fingers
    ("What other medieval torture device targeted the thumbs?", "Thumbscrew"),
    ("Pillywinks were a type of what medieval punishment device?", "Finger torture instrument"),
    # Q40: 100 Years War England vs France
    ("How many years did the Hundred Years' War actually last?", "116 years (1337-1453)"),
    ("Who was the French heroine who helped turn the tide of the Hundred Years' War?", "Joan of Arc"),
    # Q41: Myosis affects sight
    ("What is myosis (miosis) — a contraction or dilation of the pupil?", "Contraction"),
    ("What is the term for abnormal dilation of the pupil?", "Mydriasis"),
    # Q42: Lotus = software, vehicle, Egypt flower
    ("What is the national flower of India, also a lotus?", "Lotus (same flower)"),
    ("What software company made the famous 1-2-3 spreadsheet program?", "Lotus Development Corporation"),
    # Q43: Kendrick Lamar & SZA Grammy Song of Year
    ("What song did Kendrick Lamar & SZA win the Grammy Song of the Year for?", "Luther"),
    ("In what year did Kendrick Lamar win the Grammy for Song of the Year?", "2025"),
    # Q44: White belt lowest rank
    ("What color belt typically represents the highest rank in martial arts?", "Black"),
    ("In Brazilian Jiu-Jitsu, what belt comes after white?", "Blue"),
    # Q45: 128 fl oz = gallon
    ("How many pints are in a US gallon?", "8"),
    ("How many fluid ounces are in a US quart?", "32"),
    # Q46: Plantain = banana variety
    ("Is a plantain typically sweeter or starchier than a common banana?", "Starchier"),
    ("In what region of the world did plantains originate?", "Southeast Asia"),
    # Q47: Dorsal fin = back
    ("What is the fin on the belly side of a fish called?", "Pelvic fin or anal fin"),
    ("What does the dorsal fin primarily help a fish do?", "Stabilize itself in water"),
    # Q48: Pool ball 6 = green
    ("What is the color of the solid number 1 pool ball?", "Yellow"),
    ("In pool, what color is the number 7 ball?", "Maroon or brown"),
    # Q49: Tennis set minimum 6 games
    ("How many sets must a player win to win a typical men's Grand Slam tennis match?", "3"),
    ("What is a tiebreak in tennis used to determine?", "The winner of a set when games are tied 6-6"),
    # Q50: Beyoncé mother of Blue Ivy
    ("What is the name of Beyoncé's husband?", "Jay-Z"),
    ("In what year was Blue Ivy Carter born?", "2012"),
    # Q51: Thailand = Buddhism
    ("What percentage of Thailand's population is estimated to be Buddhist?", "About 95%"),
    ("What branch of Buddhism is primarily practiced in Thailand?", "Theravada Buddhism"),
    # Q52: Cyprus uses Euro
    ("In what year did Cyprus adopt the Euro?", "2008"),
    ("Cyprus is an island in what sea?", "Mediterranean Sea"),
    # Q53: Scooby Doo van = Mystery Machine
    ("What color is the Mystery Machine van?", "Green with colorful designs"),
    ("What is Scooby-Doo's full name?", "Scoobert Doobert"),
    # Q54: Odysseus home = Ithaca
    ("What is the name of Odysseus' faithful wife?", "Penelope"),
    ("How many years did Odysseus' journey home take?", "10 years"),
    # Q55: Lufthansa = Germany
    ("What is Lufthansa's primary hub airport?", "Frankfurt Airport"),
    ("What airline alliance is Lufthansa a founding member of?", "Star Alliance"),
    # Q56: Sherlock Holmes plays violin
    ("At what address did Sherlock Holmes live?", "221B Baker Street, London"),
    ("Who wrote the Sherlock Holmes stories?", "Arthur Conan Doyle"),
    # Q57: Tennessee Titans logo 3 shapes
    ("What city do the Tennessee Titans play in?", "Nashville"),
    ("What was the Tennessee Titans' original team name before moving?", "Houston Oilers"),
    # Q58: Cousteau invented aqualung
    ("In what year did Cousteau co-invent the aqualung?", "1943"),
    ("Who did Jacques Cousteau co-invent the aqualung with?", "Émile Gagnan"),
    # Q59: Fabergé = Russia
    ("What are Fabergé eggs traditionally made of?", "Precious metals and gemstones"),
    ("Who commissioned the first Fabergé Easter egg?", "Tsar Alexander III"),
    # Q60: Retinol = Vitamin A
    ("What condition is caused by severe Vitamin A deficiency?", "Night blindness"),
    ("What organ stores the most Vitamin A (retinol) in the body?", "Liver"),
    # Q61: Iris = colored part of eye
    ("What part of the eye controls how much light enters the pupil?", "Iris"),
    ("What is the clear protective covering at the front of the eye called?", "Cornea"),
    # Q62: Peking Duck = fowl
    ("In what city did Peking Duck originate?", "Beijing (Peking)"),
    ("What type of duck is traditionally used for Peking Duck?", "White Pekin duck"),
    # Q63: Pistil = female flower part
    ("What is the sticky tip of the pistil called?", "Stigma"),
    ("What is the tube connecting the stigma to the ovary in a flower?", "Style"),
    # Q64: Cinnamon from bark
    ("From what country does most of the world's true cinnamon come?", "Sri Lanka"),
    ("What is the difference between Ceylon cinnamon and Cassia cinnamon?", "Ceylon is milder and sweeter; Cassia is stronger and more common in the US"),
    # Q65: Nissan owns Infiniti
    ("What is Toyota's luxury vehicle brand?", "Lexus"),
    ("What is Honda's luxury vehicle brand?", "Acura"),
    # Q66: Caviar = sturgeon
    ("In what sea is sturgeon caviar most famously harvested?", "Caspian Sea"),
    ("What is the most expensive type of caviar called?", "Beluga caviar"),
    # Q67: Blue whale = largest animal ever
    ("How long can a blue whale grow?", "Up to 100 feet (30 meters)"),
    ("What do blue whales primarily eat?", "Krill"),
    # Q68: Euro Disney in France
    ("In what year did Disneyland Paris (formerly Euro Disney) open?", "1992"),
    ("What is the current official name of Euro Disney?", "Disneyland Paris"),
    # Q69: 270 electoral votes needed
    ("How many total electoral votes exist in the US presidential election?", "538"),
    ("How many US states plus DC contribute electoral votes?", "51 (50 states plus Washington DC)"),
    # Q70: Austin FC first MLS match 2021
    ("What stadium does Austin FC play in?", "Q2 Stadium"),
    ("What MLS conference is Austin FC in?", "Western Conference"),
    # Q71: Lakers at Crypto.com Arena
    ("What NBA team shares Crypto.com Arena with the Lakers?", "LA Clippers"),
    ("What was the Crypto.com Arena formerly known as?", "Staples Center"),
    # Q72: Eisenhower = Supreme Allied Commander WWII
    ("What was Eisenhower's popular nickname?", "Ike"),
    ("Which branch of the US military did Eisenhower serve in?", "Army"),
    # Q73: Phantom of Opera set in London
    ("Who composed The Phantom of the Opera?", "Andrew Lloyd Webber"),
    ("In what year did The Phantom of the Opera open on Broadway?", "1988"),
    # Q74: San Andreas Fault in California
    ("What type of tectonic fault is the San Andreas Fault?", "Strike-slip (transform) fault"),
    ("What two tectonic plates meet at the San Andreas Fault?", "North American Plate and Pacific Plate"),
    # Q75: Trojan Horse = Greece
    ("Which Greek hero devised the Trojan Horse strategy?", "Odysseus"),
    ("What city were the Greeks trying to conquer with the Trojan Horse?", "Troy"),
    # Q76: Don Quixote rode Rocinante
    ("Who wrote Don Quixote?", "Miguel de Cervantes"),
    ("What was the name of Don Quixote's sidekick?", "Sancho Panza"),
    # Q77: DeJoria owned Patrón
    ("What other company is John Paul DeJoria famous for co-founding?", "John Paul Mitchell Systems"),
    ("What company acquired Patrón tequila from John Paul DeJoria?", "Bacardi (2018)"),
    # Q78: Edwin Drood left unfinished by Dickens
    ("In what year did Charles Dickens die?", "1870"),
    ("How many novels did Charles Dickens complete in his lifetime?", "15"),
    # Q79: Georgia/Mississippi trick question
    ("What river forms the border between Georgia and Alabama?", "Chattahoochee River"),
    ("What state lies between Georgia and Mississippi?", "Alabama"),
    # Q80: Carpenter's square = L shape
    ("What is a carpenter's square also commonly called?", "Framing square or try square"),
    ("What material is a typical carpenter's square made from?", "Steel or aluminum"),
    # Q81: 8 quarts in a peck
    ("How many pecks are in a bushel?", "4"),
    ("How many dry quarts are in a bushel?", "32"),
    # Q82: Canada = largest N. American country
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the second largest country in the world by total area?", "Canada"),
    # Q83: Ansel Adams = photography
    ("What national park is Ansel Adams most associated with photographically?", "Yosemite"),
    ("What style of photography was Ansel Adams best known for?", "Black and white landscape photography"),
    # Q84: Charles River divides Boston/Cambridge
    ("What university is located in Cambridge across the Charles River from Boston?", "MIT (and Harvard)"),
    ("The Charles River empties into what harbor?", "Boston Harbor"),
    # Q85: Johnny Storm = Human Torch
    ("What superhero team does Johnny Storm belong to?", "Fantastic Four"),
    ("What is the name of Johnny Storm's sister in the Fantastic Four?", "Sue Storm (Invisible Woman)"),
    # Q86: Iwo Jima flag raisers = Marines
    ("Who took the famous Iwo Jima flag-raising photograph?", "Joe Rosenthal"),
    ("In what ocean is Iwo Jima located?", "Pacific Ocean"),
    # Q87: Dutch East Indies = Indonesia
    ("What is the capital of Indonesia?", "Jakarta"),
    ("How many islands make up the nation of Indonesia?", "Over 17,000"),
    # Q88: LASER A = Amplification
    ("What does the 'L' in LASER stand for?", "Light"),
    ("Who is credited with building the first working laser in 1960?", "Theodore Maiman"),
    # Q89: Washington did NOT sign Declaration
    ("Who is famous for his large signature on the Declaration of Independence?", "John Hancock"),
    ("In what year was the Declaration of Independence signed?", "1776"),
    # Q90: Female mosquitoes bite
    ("Why do only female mosquitoes bite humans?", "They need blood protein to produce eggs"),
    ("How many species of mosquitoes are there worldwide?", "Over 3,500"),
    # Q91: Pershing = WWI
    ("What was the name of the US military force in WWI commanded by General Pershing?", "American Expeditionary Forces (AEF)"),
    ("How did General Pershing earn the nickname 'Blackjack'?", "From his command of African American Buffalo Soldiers"),
    # Q92: Miami University = Ohio
    ("What is Miami University in Ohio nicknamed related to its influence on college athletics?", "Cradle of Coaches"),
    ("What state is Florida's Miami university located in?", "Florida"),
    # Q93: Hawaii postal code = HI
    ("What is the postal abbreviation for Alaska?", "AK"),
    ("What is the postal abbreviation for Illinois?", "IL"),
    # Q94: Voting age = 18
    ("What constitutional amendment lowered the US voting age to 18?", "26th Amendment"),
    ("In what year was the US voting age lowered to 18?", "1971"),
    # Q95: Fenway Park = Red Sox
    ("In what year was Fenway Park built?", "1912"),
    ("What is the famous left-field wall at Fenway Park called?", "The Green Monster"),
    # Q96: Capistrano swallows winter in Argentina
    ("In what California city do the famous swallows return each spring?", "San Juan Capistrano"),
    ("What type of swallow makes the migration to San Juan Capistrano?", "Cliff swallow"),
    # Q97: Wyoming smallest population
    ("What is the capital of Wyoming?", "Cheyenne"),
    ("What is Wyoming's official state nickname?", "The Equality State"),
    # Q98: Jonquil = yellow
    ("What plant family does the jonquil belong to?", "Amaryllidaceae (Narcissus family)"),
    ("Jonquil is a type of what common spring bulb flower?", "Narcissus or daffodil"),
    # Q99: Lambrusco = Italy
    ("From what region of Italy does Lambrusco wine originate?", "Emilia-Romagna"),
    ("Is Lambrusco wine typically still or sparkling?", "Sparkling (frizzante or spumante)"),
    # Q100: Iron Man triathlon order = swim, bike, run
    ("What is the total swimming distance in a full Ironman triathlon?", "2.4 miles (3.86 km)"),
    ("How long is the running portion of a full Ironman triathlon?", "26.2 miles (a full marathon)"),
    # Q101: Madarosis = loss of eyebrows
    ("What is the medical term for loss of eyelashes?", "Madarosis (same term covers both)"),
    ("What medical condition or treatment commonly causes madarosis?", "Alopecia, chemotherapy, or thyroid disorders"),
    # Q102: Zurich = largest Swiss city
    ("What is the capital of Switzerland?", "Bern"),
    ("On what lake is the city of Zurich situated?", "Lake Zurich"),
    # Q103: Hi-Hat = drums
    ("What are the two cymbals in a hi-hat mounted on?", "A stand with a foot pedal"),
    ("What other cymbal is essential in a standard drum kit besides the hi-hat?", "Crash cymbal and ride cymbal"),
    # Q104: KFC most outlets in China
    ("In what country did KFC (Kentucky Fried Chicken) originate?", "United States"),
    ("Who founded KFC (Kentucky Fried Chicken)?", "Colonel Harland Sanders"),
    # Q105: Boston Celtics most NBA championships
    ("How many NBA titles have the Boston Celtics won as of 2025?", "18"),
    ("Who did the Boston Celtics defeat in the 2024 NBA Finals?", "Dallas Mavericks"),
    # Q106: War of 1812 — US invaded Canada, British burned Capitol
    ("In what year was the US Capitol burned by British forces?", "1814"),
    ("What US city was the capital during the burning of the Capitol in 1814?", "Washington D.C."),
    # Q107: Little Mermaid = Ariel
    ("Who voiced Ariel in the original 1989 Disney Little Mermaid?", "Jodi Benson"),
    ("What is the name of Ariel's fish friend in The Little Mermaid?", "Flounder"),
    # Q108: Group of whales = pod (3 letters)
    ("What is a group of fish called?", "School"),
    ("What is a group of dolphins called?", "Pod"),
    # Q109: Timbuktu in Mali
    ("What ocean is Mali landlocked from?", "Atlantic (Mali is landlocked, no ocean access)"),
    ("What ancient empire had Timbuktu as a key center of Islamic learning?", "Mali Empire"),
    # Q110: Sitka = deer
    ("What is the largest species of deer in North America?", "Moose (elk/wapiti is second)"),
    ("In what US state or Canadian province is the Sitka deer primarily found?", "Pacific Northwest / Alaska to California"),
    # Q111: Texas A&M mascot = Reveille
    ("What breed of dog is Reveille, the Texas A&M mascot?", "Rough Collie"),
    ("What is the name of the University of Texas mascot?", "Bevo (a longhorn)"),
    # Q112: Malaria = Marsh Fever
    ("What type of parasite causes malaria?", "Plasmodium (a protozoan parasite)"),
    ("What insect transmits malaria?", "Female Anopheles mosquito"),
    # Q113: 1st Amendment = Freedom of Speech
    ("What other freedoms does the 1st Amendment protect besides speech?", "Religion, press, assembly, and petition"),
    ("What amendment protects against unreasonable searches and seizures?", "4th Amendment"),
    # Q114: Sprite = obey your thirst
    ("What company makes Sprite?", "The Coca-Cola Company"),
    ("In what year was Sprite first introduced?", "1961"),
    # Q115: Vaping age in Texas = 21
    ("What is the minimum age to purchase cigarettes in Texas?", "21"),
    ("In what year did the federal government raise the tobacco purchase age to 21?", "2019"),
    # Q116: Madagascar = east of Africa
    ("What is the capital of Madagascar?", "Antananarivo"),
    ("What ocean separates Madagascar from the African continent?", "Mozambique Channel (Indian Ocean)"),
    # Q117: Barbara Walters = ABC
    ("What famous TV newsmagazine show did Barbara Walters co-host?", "20/20"),
    ("What talk show did Barbara Walters co-create?", "The View"),
    # Q118: Fellmonger deals in animal skins
    ("What is a person called who makes goods from leather?", "Tanner or leather worker"),
    ("What is a person who buys and sells wool called?", "Wool stapler or wool merchant"),
    # Q119: Japan = 4 main islands
    ("What is the largest island of Japan?", "Honshu"),
    ("What is the name of the southernmost of Japan's four main islands?", "Kyushu"),
    # Q120: Buick Enclave
    ("What car company makes the Enclave SUV?", "Buick"),
    ("What is another popular Buick model that shares a name with a North American geographic feature?", "Buick LaCrosse or Buick Cascada"),
    # Q121: US moved to all-volunteer military in 1970s (1973)
    ("What system preceded the all-volunteer military in the US?", "The draft (conscription)"),
    ("The last US military draft lottery was held in what year?", "1972"),
    # Q122: Cochlea is in the ear
    ("What does the cochlea do in the human ear?", "Converts sound vibrations into nerve signals"),
    ("What is the snail-shaped structure in the inner ear called?", "Cochlea"),
    # Q123: Sting born first (Oct 1951)
    ("What band is Sting the frontman of?", "The Police"),
    ("What is Sting's real name?", "Gordon Sumner"),
    # Q124: Adams AND Jefferson signed Declaration
    ("Who was the only president to have a son also become president before the Bushes?", "John Adams (father of John Quincy Adams)"),
    ("Who was the only president to die on July 4th, the same day as John Adams?", "Thomas Jefferson (both died July 4, 1826)"),
    # Q125: D in LED = Diode
    ("What does the 'L' stand for in LED?", "Light"),
    ("What does the 'E' stand for in LED?", "Emitting"),
    # Q126: Iditarod ends in Nome, Alaska
    ("In what Alaskan city does the Iditarod dog sled race begin?", "Anchorage (ceremonial start) / Willow (official restart)"),
    ("Approximately how long is the Iditarod Trail race?", "About 1,000 miles"),
    # Q127: 5 cubed = 125
    ("What is 5 squared?", "25"),
    ("What is the cube root of 125?", "5"),
    # Q128: Red River = southern border of Oklahoma
    ("What two states does the Red River separate along its Oklahoma border?", "Oklahoma and Texas"),
    ("Into what larger river does the Red River of the South flow?", "Mississippi River"),
    # Q129: SNL has most Emmys (50)
    ("In what year did Saturday Night Live premiere?", "1975"),
    ("Who was the original creator of Saturday Night Live?", "Lorne Michaels"),
    # Q130: Watergate Burglars = Gonzalez etc.
    ("In what year did the Watergate break-in occur?", "1972"),
    ("What president was involved in the Watergate scandal?", "Richard Nixon"),
    # Q131: West Virginia = The Mountain State
    ("What is West Virginia's state motto?", "Montani Semper Liberi (Mountaineers Are Always Free)"),
    ("West Virginia became a state by seceding from which Confederate state?", "Virginia"),
    # Q132: NBC broadcast most recent Super Bowl (Super Bowl 60, 2026)
    ("What channel broadcast Super Bowl 59 (February 2025)?", "Fox"),
    ("In what city was Super Bowl 60 (2026) held?", "New Orleans, Louisiana"),
    # Q133: Buzz Aldrin = second on moon
    ("Who was the first human to walk on the moon?", "Neil Armstrong"),
    ("What was the name of the Apollo 11 mission commander?", "Neil Armstrong"),
    # Q134: Florida extends farther south than Texas tip
    ("What is the southernmost city in the continental United States?", "Key West, Florida"),
    ("What is the name of the southernmost tip of Florida?", "Key West"),
    # Q135: Kentucky Derby winner Golden Tempo (2026)
    ("In what city is the Kentucky Derby held?", "Louisville, Kentucky"),
    ("What racetrack hosts the Kentucky Derby?", "Churchill Downs"),
    # Q136: Frank Broyles Award = outstanding assistant coach
    ("Who is the Frank Broyles Award named after?", "Frank Broyles, former Arkansas football coach and AD"),
    ("In what sport is the Frank Broyles Award presented?", "College football"),
    # Q137: Caliber = internal diameter of gun bore
    ("What unit is caliber typically measured in?", "Hundredths of an inch or millimeters"),
    ("What is the caliber of the common .45 ACP handgun round in millimeters?", "11.43 mm"),
    # Q138: Billy the Kid alive 1859-1881
    ("In what year was Billy the Kid killed?", "1881"),
    ("Who killed Billy the Kid?", "Sheriff Pat Garrett"),
    # Q139: Spirit of St. Louis in Washington DC
    ("Who flew the Spirit of St. Louis on the first nonstop transatlantic flight?", "Charles Lindbergh"),
    ("In what year did Charles Lindbergh make his famous transatlantic flight?", "1927"),
    # Q140: Pearl Harbor bombing = December
    ("In what year was Pearl Harbor attacked?", "1941"),
    ("What country carried out the attack on Pearl Harbor?", "Japan"),
    # Q141: AT&T Stadium, Arlington TX (Cowboys)
    ("What NFL team plays at AT&T Stadium in Arlington, Texas?", "Dallas Cowboys"),
    ("In what year did AT&T Stadium (Cowboys) open?", "2009"),
    # Q142: Mojave Desert majority in California
    ("In what other US state is a portion of the Mojave Desert located?", "Nevada, Utah, and Arizona"),
    ("What famous road passes through the Mojave Desert?", "Route 66"),
    # Q143: Oprah Winfrey 0 Oscars
    ("For what film was Oprah Winfrey nominated for an Academy Award?", "The Color Purple (1986)"),
    ("What is Oprah Winfrey's production company called?", "Harpo Productions"),
    # Q144: Harry Potter's scar = lightning bolt
    ("What caused Harry Potter's lightning bolt scar?", "Voldemort's killing curse (Avada Kedavra)"),
    ("On what part of Harry Potter's body is his scar located?", "Forehead"),
    # Q145: Van Damme first name = Jean-Claude
    ("What nationality is actor Jean-Claude Van Damme?", "Belgian"),
    ("Jean-Claude Van Damme is primarily known for what type of movies?", "Martial arts action films"),
    # Q146: UN flag = blue
    ("What image is on the UN flag besides the blue background?", "A world map encircled by olive branches"),
    ("In what US city is the United Nations headquarters located?", "New York City"),
    # Q147: Franklin = first Black Peanuts character 1968
    ("Who created the Peanuts comic strip?", "Charles M. Schulz"),
    ("What is the name of the bald-headed boy in Peanuts?", "Charlie Brown"),
    # Q148: Capricorn = goat
    ("What are the dates of the Capricorn zodiac sign?", "December 22 to January 19"),
    ("What zodiac sign follows Capricorn?", "Aquarius"),
    # Q149: Beckham's kid Romeo named from Shakespeare
    ("What Shakespeare play does the name Romeo come from?", "Romeo and Juliet"),
    ("What are David Beckham's four children's names?", "Brooklyn, Romeo, Cruz, Harper"),
    # Q150: Spaceship Earth at Epcot
    ("What theme park is Spaceship Earth located in?", "Epcot (Walt Disney World)"),
    ("What geometric shape is the Spaceship Earth structure at Epcot?", "Geodesic sphere"),
    # Q151: Cleveland on Lake Erie
    ("What is the capital of Ohio?", "Columbus"),
    ("What other major city sits on the southern shore of Lake Erie?", "Buffalo, New York"),
    # Q152: Taylor Swift fans = Swifties
    ("What is the fan base of Beyoncé called?", "BeyHive"),
    ("What is the fan base of Lady Gaga called?", "Little Monsters"),
    # Q153: Beyoncé country album = Cowboy Carter (2024)
    ("What Grammy did Beyoncé's Cowboy Carter album win?", "Album of the Year (2025)"),
    ("What was Beyoncé's previous studio album before Cowboy Carter?", "Renaissance (2022)"),
    # Q154: Androcles pulled thorn from lion's paw
    ("What ancient Greek storyteller is credited with the fable of Androcles and the Lion?", "Aesop"),
    ("What is the moral of the story of Androcles and the Lion?", "Gratitude; kindness is rewarded"),
    # Q155: Getty Museum in California (LA)
    ("How many Getty Museum locations are in the Los Angeles area?", "2 (Getty Center and Getty Villa)"),
    ("Who was J. Paul Getty?", "American oil tycoon and art collector"),
    # Q156: Eagle Pass across from Piedras Negras, Mexico
    ("In what US state is the city of Eagle Pass located?", "Texas"),
    ("What river separates Eagle Pass, Texas from Piedras Negras, Mexico?", "Rio Grande"),
    # Q157: Gobi Desert in China and Mongolia
    ("On what continent is the Gobi Desert located?", "Asia"),
    ("What is the Gobi Desert primarily covered by — sand dunes or rocky terrain?", "Rocky terrain (desert pavement)"),
    # Q158: Rembrandt went by first name only
    ("What was Rembrandt's full name?", "Rembrandt Harmenszoon van Rijn"),
    ("What country was Rembrandt from?", "Netherlands (Dutch)"),
    # Q159: Miss Marple's first name = Jane
    ("Who created the character of Miss Marple?", "Agatha Christie"),
    ("In what English village does Miss Marple live?", "St. Mary Mead"),
    # Q160: EuroDisney in France (duplicate of Q68 — still need challenges)
    ("What is the French town nearest to Disneyland Paris?", "Chessy (Marne-la-Vallée)"),
    ("What Disney character is most prominently featured at Disneyland Paris?", "Mickey Mouse"),
    # Q161: Minimum electoral votes 270 (duplicate — need different challenges)
    ("What happens if no presidential candidate reaches 270 electoral votes?", "The House of Representatives chooses the president"),
    ("Which state has the most electoral votes?", "California (54)"),
    # Q162: Most lemurs on Madagascar / Africa
    ("Madagascar is part of which continent politically and geographically?", "Africa"),
    ("Are lemurs found in the wild anywhere outside of Madagascar?", "No, they are endemic to Madagascar"),
    # Q163: Austin FC 2021 (duplicate)
    ("What jersey colors do Austin FC wear?", "Verde (green) and black"),
    ("What is the name of Austin FC's primary supporters group?", "Austin Anthem or La Murga de Austin"),
    # Q164: Lakers at Crypto.com Arena (duplicate)
    ("How many NBA championships have the Los Angeles Lakers won?", "17"),
    ("Who is the all-time leading scorer for the Los Angeles Lakers?", "LeBron James"),
    # Q165: Eisenhower Supreme Allied Commander (duplicate)
    ("In what year did Dwight Eisenhower become US President?", "1953"),
    ("Who succeeded Eisenhower as US President?", "John F. Kennedy"),
    # Q166: Phantom of Opera in London (duplicate)
    ("In what year did Phantom of the Opera first open in London's West End?", "1986"),
    ("Phantom of the Opera is based on a novel by what author?", "Gaston Leroux"),
    # Q167: San Andreas Fault in California (duplicate)
    ("When was the last major earthquake caused by the San Andreas Fault?", "1906 (San Francisco earthquake)"),
    ("How long is the San Andreas Fault?", "About 800 miles (1,300 km)"),
    # Q168: Trojan Horse = Greece (duplicate)
    ("According to Homer, what was the name of the Greek king who led the Trojan War?", "Agamemnon"),
    ("How long did the Trojan War allegedly last according to Greek mythology?", "10 years"),
    # Q169: Don Quixote / Rocinante (duplicate)
    ("In what language was Don Quixote originally written?", "Spanish"),
    ("What does the name Rocinante mean in Spanish?", "Former packhorse (or horse that was once a workhorse)"),
    # Q170: DeJoria/Patrón (duplicate)
    ("What type of agave is Patrón tequila made from?", "Blue Weber agave"),
    ("In what Mexican state is Patrón tequila produced?", "Jalisco"),
    # Q171: Dickens / Edwin Drood (duplicate)
    ("What is Charles Dickens' best-known novel?", "A Tale of Two Cities or Oliver Twist"),
    ("How many parts had Dickens completed of Edwin Drood before he died?", "6 of 12 planned"),
    # Q172: Georgia/Mississippi trick question (duplicate)
    ("How many US states border Mississippi?", "4 (Tennessee, Alabama, Louisiana, Arkansas)"),
    ("What is the capital of Georgia?", "Atlanta"),
    # Q173: Mila Kunis voices Meg Griffin in Family Guy
    ("Since what year has Mila Kunis voiced Meg Griffin in Family Guy?", "1999 (Season 2, replacing Lacey Chabert)"),
    ("Who voices Peter Griffin in Family Guy?", "Seth MacFarlane"),
    # Q174: Carpenter's square = L shape (duplicate)
    ("What is the corner of an L-shaped carpenter's square called?", "The heel"),
    ("What does a carpenter's square help ensure when building?", "Right angles (90 degrees)"),
    # Q175: 8 quarts in peck (duplicate)
    ("How many fluid ounces are in a quart?", "32"),
    ("How many cups are in a peck?", "32"),
    # Q176: Canada largest N. American country (duplicate)
    ("What is Canada's most populous city?", "Toronto"),
    ("What is the only country that borders Canada to the south?", "United States"),
    # Q177: Ansel Adams / photography (duplicate)
    ("What technique, involving darkroom manipulation, did Ansel Adams help develop?", "Zone System"),
    ("In what decade was Ansel Adams born?", "1900s (1902)"),
    # Q178: Charles River / Boston (duplicate)
    ("What is the name of the regatta held annually on the Charles River?", "Head of the Charles Regatta"),
    ("In what city does the Charles River originate?", "Hopkinton, Massachusetts"),
    # Q179: Johnny Storm / Human Torch (duplicate)
    ("What is the Human Torch's battle cry?", "Flame on!"),
    ("What material is the Human Torch (Johnny Storm) immune to?", "Fire"),
    # Q180: Don Pedro de Peralta / Santa Fe
    ("What is the capital of New Mexico?", "Santa Fe"),
    ("Santa Fe is the oldest state capital in the continental US — in what year was it founded?", "1610"),
    # Q181: Iwo Jima / Marines (duplicate)
    ("In what WWII battle was the famous Iwo Jima flag-raising photo taken?", "Battle of Iwo Jima"),
    ("In what year did the Battle of Iwo Jima take place?", "1945"),
    # Q182: Indonesia = Dutch East Indies (duplicate)
    ("What is Indonesia's most populous city?", "Jakarta"),
    ("In what year did Indonesia gain independence from the Netherlands?", "1945"),
    # Q183: LASER A = Amplification (duplicate)
    ("What does the 'S' in LASER stand for?", "Stimulated"),
    ("In what year was the first working laser demonstrated?", "1960"),
    # Q184: 4 umpires in MLB game
    ("How many umpires are on the field during MLB playoff games?", "6"),
    ("What do umpires use to keep track of balls and strikes during a game?", "Clicker/indicator"),
    # Q185: CAD D = Design
    ("What does the 'C' in CAD stand for?", "Computer"),
    ("What does the 'A' in CAD stand for?", "Aided"),
    # Q186: Earth larger than Mars
    ("How many times larger is Earth's diameter compared to Mars'?", "About 1.9 times"),
    ("What color is Mars due to its iron oxide surface?", "Red"),
    # Q187: Gerald Ford pardoned Nixon
    ("What was Richard Nixon's middle name?", "Milhous"),
    ("How many years after resigning did Richard Nixon live?", "20 years (1974-1994)"),
    # Q188: 30 MPH ≈ 48 km/h
    ("How many kilometers per hour is 60 MPH?", "About 96.6 km/h"),
    ("What country primarily uses miles per hour instead of km/h?", "United States and United Kingdom"),
    # Q189: Golf Grand Slam = 4 tournaments
    ("What are the 4 major golf tournaments in the Grand Slam?", "Masters, US Open, The Open (British Open), PGA Championship"),
    ("What golfer has won the most career major golf championships?", "Jack Nicklaus (18 majors)"),
    # Q190: RPG = Role-Playing Game
    ("What does FPS stand for in video games?", "First-Person Shooter"),
    ("What does MMO stand for in video games?", "Massively Multiplayer Online"),
    # Q191: Port side = red navigation light
    ("What color is the starboard navigation light on a vessel?", "Green"),
    ("Which side is the starboard side of a ship — left or right when facing forward?", "Right"),
    # Q192: Bicycle = mode of transport and playing card brand
    ("What is the most popular brand of playing cards in the United States?", "Bicycle (USPC)"),
    ("In what year did the US Playing Card Company introduce Bicycle cards?", "1885"),
    # Q193: Camp David in Maryland
    ("What is the official name of Camp David?", "Naval Support Facility Thurmont"),
    ("Which president established Camp David and gave it its current name?", "Dwight Eisenhower (named for grandson David)"),
    # Q194: Gaza Strip on Mediterranean Sea
    ("What two political entities control the Gaza Strip?", "Hamas (governing) and Israel (blockade)"),
    ("How long is the Gaza Strip from north to south?", "About 25 miles (40 km)"),
    # Q195: Hydra killed by Hercules
    ("What was the Lernaean Hydra's most dangerous characteristic?", "Growing two heads for every one cut off"),
    ("Who helped Hercules kill the Hydra by cauterizing the necks?", "Iolaus (his nephew)"),
    # Q196: US motto since 1956 = 'In God We Trust'
    ("What was the US national motto before 'In God We Trust'?", "E pluribus unum (out of many, one)"),
    ("In what year did 'In God We Trust' appear on US coins for the first time?", "1864"),
    # Q197: Howard Stern in Private Parts
    ("In what year was the movie Private Parts (Howard Stern) released?", "1997"),
    ("What radio station is Howard Stern currently on?", "SiriusXM (Sirius XM Satellite Radio)"),
    # Q198: Quiver = proper name for arrow container
    ("What is the name for the container that holds a bow?", "Bow case (there is no special single word)"),
    ("How many arrows does a standard archery quiver hold?", "Typically 12-24 arrows"),
    # Q199: Quakers founded Philadelphia
    ("Who was the founder of the Quaker faith?", "George Fox"),
    ("What is the formal name for the Quaker religion?", "Religious Society of Friends"),
    # Q200: Lady Godiva statue in Coventry, England
    ("What was the legendary reason Lady Godiva rode naked through Coventry?", "To protest her husband's oppressive taxation"),
    ("Who peeped at Lady Godiva during her ride, giving us the term 'Peeping Tom'?", "Tom (a tailor in the legend)"),
    # Q201: VP plane = Air Force Two
    ("What is the call sign of the US President's helicopter?", "Marine One"),
    ("What type of aircraft is typically used as Air Force Two?", "Boeing C-32 (modified Boeing 757)"),
    # Q202: Ellen DeGeneres = EGOT (Oscar, Emmy, Grammy, Tony)
    ("What does EGOT stand for?", "Emmy, Grammy, Oscar, Tony"),
    ("Who was the first person to win an EGOT?", "Helen Hayes (1977)"),
    # Q203: 20/20 vision numerator = 20
    ("What does 20/20 vision mean?", "You can see at 20 feet what a person with normal vision sees at 20 feet"),
    ("What does 20/200 vision mean and what is it associated with?", "Legal blindness — seeing at 20 feet what normal vision sees at 200 feet"),
    # Q204: Chile owns southernmost point of South America
    ("What is the name of the southernmost city in the world?", "Ushuaia, Argentina (or Puerto Williams, Chile)"),
    ("What is the name of the southernmost tip of South America?", "Cape Horn"),
    # Q205: Bin Laden buried at sea
    ("In what year was Osama bin Laden killed?", "2011"),
    ("In what country was Osama bin Laden found and killed?", "Pakistan"),
    # Q206: Random Task = Austin Powers villain 'Odd Job' take
    ("What James Bond film featured the original villain Odd Job?", "Goldfinger (1964)"),
    ("What did Odd Job use as his signature weapon?", "A razor-edged bowler hat"),
    # Q207: Book of Mormon won Tony = Trey Parker & Matt Stone
    ("What TV show did Trey Parker and Matt Stone create?", "South Park"),
    ("How many Tony Awards did The Book of Mormon win?", "9 Tony Awards"),
    # Q208: Stalemate in chess
    ("In chess, what is the term for a complete draw where neither side can checkmate?", "Draw"),
    ("How many squares does a standard chess board have?", "64"),
    # Q209: Jason and Argonauts sought Golden Fleece
    ("What ship did Jason and the Argonauts sail on?", "The Argo"),
    ("In what modern country is the mythical land of Colchis, where the Golden Fleece was kept?", "Georgia (the country)"),
    # Q210: Monopoly houses = green
    ("What color are hotels in standard Monopoly?", "Red"),
    ("How many houses must you own before building a hotel in Monopoly?", "4"),
    # Q211: CAD D = Design (duplicate)
    ("What is AutoCAD primarily used for?", "Computer-aided design and drafting"),
    ("What company makes AutoCAD software?", "Autodesk"),
    # Q212: Obama first president not born in 48 contiguous states
    ("In what Hawaiian city was Barack Obama born?", "Honolulu"),
    ("Who was the first US president born in a state west of the Mississippi?", "Herbert Hoover (born in Iowa)"),
    # Q213: Millie Bobby Brown = No. 11 in Stranger Things
    ("What character does Millie Bobby Brown play in Stranger Things?", "Eleven (El)"),
    ("In what year did Stranger Things first premiere?", "2016"),
    # Q214: 4 pecks in a bushel
    ("How many quarts are in one peck?", "8"),
    ("What is a bushel typically used to measure?", "Dry goods like grain, produce"),
    # Q215: Lent = 40 days
    ("What Christian holiday marks the end of the Lenten season?", "Easter"),
    ("What day marks the beginning of Lent?", "Ash Wednesday"),
    # Q216: Squirrel lives in a drey
    ("What do you call a squirrel's nest?", "Drey"),
    ("What is the name for a beaver's home?", "Lodge"),
    # Q217: David Evans (The Edge) of U2
    ("What is the Edge's role in U2?", "Lead guitarist"),
    ("What is U2's lead singer's name?", "Bono (Paul Hewson)"),
    # Q218: RTS = Real-Time Strategy
    ("What does MOBA stand for in video games?", "Multiplayer Online Battle Arena"),
    ("What is the most popular RTS game series of all time?", "StarCraft or Command & Conquer"),
    # Q219: Glaswegian = from Glasgow
    ("What is someone from Edinburgh called?", "Edinburger or Edinburghian"),
    ("What country is Glasgow located in?", "Scotland"),
    # Q220: GORP = trail mix
    ("What does GORP stand for?", "Good Old Raisins and Peanuts"),
    ("What is another common name for GORP?", "Trail mix"),
    # Q221: Costa Rica currency = Colon (body part)
    ("What is the capital of Costa Rica?", "San José"),
    ("The Costa Rican colón is named after which explorer?", "Christopher Columbus (Cristóbal Colón)"),
    # Q222: Gadsden Flag has rattlesnake
    ("What phrase is printed on the Gadsden Flag?", "Don't Tread On Me"),
    ("What color is the background of the Gadsden Flag?", "Yellow"),
    # Q223: Corpulent = plump
    ("What is the antonym of corpulent?", "Lean, thin, or slender"),
    ("What is another word for corpulent meaning the same thing?", "Obese, stout, or rotund"),
    # Q224: Silly Putty invented 1943 by James Wright
    ("What company marketed Silly Putty beginning in 1950?", "Crayola"),
    ("What was Silly Putty originally made from?", "Silicone oil and boric acid"),
    # Q225: Lima and Quebec in NATO phonetic alphabet
    ("What word represents the letter 'A' in the NATO phonetic alphabet?", "Alpha"),
    ("What word represents the letter 'Z' in the NATO phonetic alphabet?", "Zulu"),
    # Q226: BHP = Brake Horsepower
    ("What does HP stand for in engine terminology?", "Horsepower"),
    ("What does the 'B' in BHP stand for?", "Brake"),
    # Q227: Sumo ring = circle
    ("What is the surface material of a sumo wrestling ring?", "Sand or clay (on a raised platform called a dohyo)"),
    ("What is the name of the raised platform on which sumo is wrestled?", "Dohyo"),
    # Q228: US bought Virgin Islands from Denmark 1916
    ("How much did the US pay Denmark for the Virgin Islands in 1916?", "$25 million in gold"),
    ("What is the capital of the US Virgin Islands?", "Charlotte Amalie"),
    # Q229: Taylor Swift 'I Knew You Were Trouble' not a movie song
    ("On what Taylor Swift album does 'I Knew You Were Trouble' appear?", "Red (2012)"),
    ("Who produced 'I Knew You Were Trouble' with Taylor Swift?", "Max Martin and Shellback"),
    # Q230: Mite = not an insect (arachnid)
    ("How many legs does a mite have?", "8 (as an arachnid)"),
    ("What other common creature is an arachnid like a mite?", "Spider, tick, scorpion"),
    # Q231: Roll of nickels = $2.00
    ("How many nickels are in a roll?", "40"),
    ("How many quarters are in a standard roll?", "40 ($10 worth)"),
    # Q232: 21st Amendment repealed 18th (Prohibition)
    ("In what year did Prohibition begin in the US?", "1920"),
    ("In what year did Prohibition end in the US?", "1933"),
    # Q233: Tomato = 'love apple' in French
    ("What is the scientific classification of a tomato — fruit or vegetable botanically?", "Fruit (botanically a berry)"),
    ("From what language did the word 'tomato' originate?", "Nahuatl (Aztec language)"),
    # Q234: Demersal = lives in sea (bottom)
    ("What term describes fish that live near the ocean floor?", "Demersal or benthic"),
    ("What is the opposite of demersal for fish that live near the surface?", "Pelagic"),
    # Q235: Carnegie Hall in NYC
    ("Who funded the construction of Carnegie Hall?", "Andrew Carnegie"),
    ("In what year was Carnegie Hall opened?", "1891"),
    # Q236: Modern baseball uses cowhide (since 1974)
    ("What was used to cover baseballs before cowhide?", "Horsehide"),
    ("How many stitches does a Major League Baseball have?", "108"),
    # Q237: 12 pairs of ribs in humans
    ("How many ribs in the human body are 'floating' (not attached to the sternum)?", "2 pairs (4 ribs)"),
    ("What are the ribs that attach directly to the sternum called?", "True ribs"),
    # Q238: Nintendo introduced Mario
    ("In what year did Mario first appear in a Nintendo game?", "1981 (Donkey Kong)"),
    ("What was Mario's original name when he first appeared in Donkey Kong?", "Jumpman"),
    # Q239: Infiniti is luxury brand of Nissan (duplicate)
    ("In what year was Infiniti launched as a luxury brand?", "1989"),
    ("What does the Infiniti logo represent?", "A road leading to infinity"),
    # Q240: American Idol introduced Clarkson and Underwood
    ("What year did Kelly Clarkson win the first season of American Idol?", "2002"),
    ("What season of American Idol did Carrie Underwood win?", "Season 4 (2005)"),
    # Q241: 3 presidential libraries in Texas
    ("Which 3 US presidents have their presidential libraries in Texas?", "LBJ, George H.W. Bush, George W. Bush"),
    ("Where is the LBJ Presidential Library located?", "Austin, Texas (UT Austin campus)"),
    # Q242: Lady Gaga fans = Little Monsters
    ("What is Lady Gaga's real name?", "Stefani Joanne Angelina Germanotta"),
    ("In what year did Lady Gaga release her debut album 'The Fame'?", "2008"),
    # Q243: $5 casino chip = red
    ("What color is a $25 casino chip in most Las Vegas casinos?", "Green"),
    ("What color is a $100 casino chip in most Las Vegas casinos?", "Black"),
    # Q244: Worcestershire Sauce contains anchovies
    ("In what English county was Worcestershire Sauce invented?", "Worcestershire"),
    ("What other common condiment besides Worcestershire Sauce traditionally contains anchovies?", "Caesar salad dressing"),
    # Q245: Sancho Panza = companion of Don Quixote
    ("What does 'Sancho Panza' mean in Spanish?", "Sancho Belly (Panza means belly)"),
    ("Who created the characters of Don Quixote and Sancho Panza?", "Miguel de Cervantes"),
    # Q246: 8 US states still have electric chair
    ("When was the electric chair first used as a method of execution in the US?", "1890"),
    ("In what US state was the first electric chair execution carried out?", "New York"),
    # Q247: Ted Lasso brings 'biscuits'
    ("Who plays Ted Lasso in the Apple TV+ series?", "Jason Sudeikis"),
    ("What fictional English football club does Ted Lasso coach?", "AFC Richmond"),
    # Q248: Lake Superior = Gitche Gumee
    ("What is the largest of the five Great Lakes by surface area?", "Lake Superior"),
    ("Who used the name 'Gitche Gumee' for Lake Superior in a famous poem?", "Henry Wadsworth Longfellow"),
    # Q249: Wrangler clothing brand = animal handler
    ("What sport or activity is the Wrangler clothing brand most associated with?", "Rodeo and western/cowboy culture"),
    ("What is another meaning of the word 'wrangler' besides a cowboy?", "Someone who handles or argues about something; also a Cambridge honors graduate"),
    # Q250: Kendrick Lamar only rapper with Pulitzer Prize
    ("In what year did Kendrick Lamar win the Pulitzer Prize?", "2018"),
    ("What Kendrick Lamar album won the Pulitzer Prize?", "DAMN."),
    # Q251: Sony/Japan introduced PlayStation 1995
    ("In what year did the original PlayStation launch in the US?", "1995"),
    ("What was Sony's follow-up to the original PlayStation?", "PlayStation 2 (2000)"),
    # Q252: Satay sauce main ingredient = peanut
    ("What country is satay (peanut sauce) most associated with?", "Indonesia, Malaysia, and Thailand"),
    ("What other common condiment also uses peanuts as a key ingredient?", "Pad Thai sauce or gado-gado"),
    # Q253: Piranha native to South America
    ("In what South American river are piranhas most commonly found?", "Amazon River"),
    ("How many species of piranha exist?", "About 30-60 species"),
    # Q254: Von Trapp family = 7 kids
    ("What is the name of the musical based on the Von Trapp family?", "The Sound of Music"),
    ("Who wrote the songs for The Sound of Music?", "Rodgers and Hammerstein"),
    # Q255: Jamestown = first permanent English settlement 1607
    ("In what year was Jamestown, the first permanent English settlement, founded?", "1607"),
    ("On what river was Jamestown, Virginia founded?", "James River"),
    # Q256: House of Grimaldi = Monaco
    ("What is the official title of Monaco's ruler?", "Prince (or Princess)"),
    ("What is Monaco's official language?", "French"),
    # Q257: 5 basic ballet foot positions
    ("How many basic arm positions are there in classical ballet?", "5 or 6 (varies by school)"),
    ("In what country did classical ballet originate?", "France (with Italian roots)"),
    # Q258: Vitamin D from sunlight
    ("What is the medical condition caused by Vitamin D deficiency in children?", "Rickets"),
    ("What form of Vitamin D does sunlight help the body produce?", "Vitamin D3 (cholecalciferol)"),
    # Q259: Trojan Horse soldiers from Greece (duplicate)
    ("What wooden structure did the Greeks use to sneak into Troy?", "The Trojan Horse"),
    ("Approximately when did the Trojan War take place according to historians?", "Around 1200 BCE"),
    # Q260: Skylab launched in 1970s (1973)
    ("In what year did Skylab re-enter Earth's atmosphere and burn up?", "1979"),
    ("How many astronaut crews visited America's first space station Skylab?", "3"),
    # Q261: Hamlet said 'To be or not to be'
    ("In which act of Hamlet does the 'To be or not to be' soliloquy appear?", "Act III, Scene 1"),
    ("Who wrote the play Hamlet?", "William Shakespeare"),
    # Q262: Pig fastest ground runner among pig, Road Runner, wild turkey
    ("What is the top running speed of a domestic pig?", "About 11 mph (17.7 km/h)"),
    ("What is the running speed of a wild turkey?", "About 12-20 mph — actually faster than pigs in most sources"),
    # Q263: KC Chiefs tied with Patriots at 6 Super Bowl wins
    ("How many Super Bowl losses have the Kansas City Chiefs had?", "2 (in Super Bowl I/1967 and Super Bowl LV/2021... actually 3 losses)"),
    ("Who is the head coach of the Kansas City Chiefs?", "Andy Reid"),
    # Q264: US Women's soccer won 2019 FIFA against Netherlands
    ("Who was the coach of the US Women's National Team at the 2019 World Cup?", "Jill Ellis"),
    ("What was the score of the 2019 Women's World Cup final?", "2-0 (USA over Netherlands)"),
    # Q265: Hatfield-McCoy feud in Kentucky and West Virginia
    ("What started the Hatfield-McCoy feud?", "Disputes over Civil War loyalties, a hog, and land"),
    ("Approximately when did the Hatfield-McCoy feud take place?", "1863-1891"),
    # Q266: Green Day frontman = Billie Joe Armstrong
    ("In what city was the band Green Day formed?", "Oakland/Berkeley, California"),
    ("What was Green Day's breakthrough album in 1994?", "Dookie"),
    # Q267: Sam Houston governor of Tennessee AND Texas
    ("What was Sam Houston's role in Texas history?", "First and third President of the Republic of Texas; first and third governor"),
    ("Who was Sam Houston's famous predecessor as governor of Tennessee?", "Andrew Jackson (earlier, David Crockett's nemesis)"),
    # Q268: Switzerland uses Swiss Franc, not Euro
    ("What is the currency of Switzerland called?", "Swiss Franc"),
    ("Is Switzerland a member of the European Union?", "No"),
    # Q269: First female in space was Soviet (Valentina Tereshkova, 1963)
    ("What was Valentina Tereshkova's spacecraft name on her historic 1963 spaceflight?", "Vostok 6"),
    ("In what year did the first American woman go to space?", "1983 (Sally Ride)"),
    # Q270: E=MC² — M = Mass
    ("In E=MC², what does 'E' stand for?", "Energy"),
    ("In E=MC², what does 'C' stand for?", "Speed of light in a vacuum"),
    # Q271: Scottie Scheffler was #1 golfer in 2025
    ("In what year did Scottie Scheffler win his first Masters Tournament?", "2022"),
    ("What tour does Scottie Scheffler play on primarily?", "PGA Tour"),
    # Q272: Oxymoron = 2 contradictory words
    ("What literary device involves a contradiction within a single phrase?", "Oxymoron"),
    ("Give an example of an oxymoron besides 'jumbo shrimp'.", "Pretty ugly, living dead, deafening silence"),
    # Q273: Kate Hudson's mother = Goldie Hawn
    ("What is Kate Hudson's most famous film?", "Almost Famous (2000)"),
    ("What actress/comedian was Goldie Hawn's longtime partner?", "Kurt Russell"),
    # Q274: Paul Revere wore tri-corn hat
    ("What was Paul Revere's famous midnight ride warning?", "The British are coming (or 'The Regulars are out!')"),
    ("What was Paul Revere's profession besides patriot?", "Silversmith"),
    # Q275: Shuttlecock in badminton
    ("What is the informal name for a shuttlecock?", "Birdie"),
    ("What are badminton rackets traditionally made of?", "Carbon fiber, aluminum, or steel"),
    # Q276: Andrew Johnson bought Alaska from Russia
    ("In what year did the US purchase Alaska from Russia?", "1867"),
    ("What was the US purchase of Alaska from Russia nicknamed?", "Seward's Folly (or Seward's Icebox)"),
    # Q277: National animal of Scotland = Unicorn
    ("What is the national animal of England?", "Lion"),
    ("What is the national animal of Wales?", "Dragon (red dragon)"),
    # Q278: Last Confederate state to rejoin Union = Georgia (1870)
    ("What was the last Confederate state to be readmitted to the Union?", "Georgia (1870)"),
    ("In what year did the last Confederate state be readmitted to the Union?", "1870"),
    # Q279: Green Monster at Fenway Park
    ("How tall is the Green Monster at Fenway Park?", "37 feet 2 inches"),
    ("In what year was the Green Monster's famous manual scoreboard installed?", "1934"),
    # Q280: Pedal shares name with 'Cycle' clothing
    ("What clothing brand uses the word 'cycle' in its name?", "Cycle (various) or Pedal clothing"),
    ("What is the most well-known cycling clothing brand?", "Rapha, Castelli, or Specialized"),
    # Q281: Pawn can never move backward in chess
    ("When a pawn reaches the other end of the board in chess, what can it become?", "Any piece except a king (usually a queen)"),
    ("How many pawns does each player start with in chess?", "8"),
    # Q282: L'Oréal — 'Because you're worth it' since 1970
    ("What country is L'Oréal headquartered in?", "France"),
    ("What year was L'Oréal founded?", "1909"),
    # Q283: Friday Night Lights = Odessa, Texas
    ("What is the name of the Odessa, Texas high school football team in Friday Night Lights?", "Permian Panthers"),
    ("Who wrote the book Friday Night Lights?", "H.G. Bissinger"),
    # Q284-308: S7 (mostly duplicates)
    ("In what year was Skylab deorbited?", "1979"),
    ("In what Australian city did Skylab debris land?", "Esperance, Western Australia"),
    # Q285: Hamlet 'To be or not to be' (duplicate)
    ("In what Hamlet scene does 'To be or not to be' appear?", "Act 3, Scene 1"),
    ("Who was Hamlet's father?", "King Hamlet (the ghost)"),
    # Q286: Pig fastest runner (duplicate)
    ("What is the fastest running bird?", "Ostrich"),
    ("Can a Road Runner bird actually run fast?", "Yes, about 20 mph (32 km/h)"),
    # Q287: KC Chiefs tied with Patriots 6 Super Bowls (duplicate)
    ("In what city do the Kansas City Chiefs play their home games?", "Kansas City, Missouri"),
    ("What is the name of the Kansas City Chiefs' stadium?", "Arrowhead Stadium"),
    # Q288: US Women beat Netherlands 2019 (duplicate)
    ("In what country was the 2019 Women's FIFA World Cup held?", "France"),
    ("Who scored the opening goal of the 2019 Women's World Cup Final for the US?", "Megan Rapinoe"),
    # Q289: Hatfield-McCoy feud (duplicate)
    ("What two families were involved in the famous Appalachian feud?", "Hatfields and McCoys"),
    ("Where did most of the Hatfield-McCoy feud violence take place?", "Along the Tug Fork river between Kentucky and West Virginia"),
    # Q290: Green Day frontman (duplicate)
    ("What is Green Day drummer Tré Cool's real name?", "Frank Edwin Wright III"),
    ("What genre of music is Green Day associated with?", "Punk rock / pop punk"),
    # Q291: Sam Houston governor of TN and TX (duplicate)
    ("In what year did Sam Houston become the first president of the Republic of Texas?", "1836"),
    ("Sam Houston opposed what major political act by the Texas legislature in 1861?", "Secession from the Union"),
    # Q292: Switzerland uses Swiss Franc (duplicate)
    ("When was Switzerland last at war with another nation?", "1847 (Sonderbund War, a brief civil conflict)"),
    ("What is Switzerland famous for in terms of international banking?", "Banking secrecy and neutrality"),
    # Q293: Tereshkova first female in space (duplicate)
    ("How old was Valentina Tereshkova when she went to space?", "26"),
    ("How many days did Valentina Tereshkova spend in orbit?", "Almost 3 days (70.8 hours)"),
    # Q294: E=MC² M=Mass (duplicate)
    ("Who proposed the equation E=MC²?", "Albert Einstein"),
    ("In what year did Einstein propose his theory of special relativity including E=MC²?", "1905"),
    # Q295: Scottie Scheffler #1 golfer 2025 (duplicate)
    ("What city is Scottie Scheffler from?", "Dallas, Texas"),
    ("How many PGA Tour wins did Scottie Scheffler have as of 2025?", "More than 10 wins"),
    # Q296: Clothing label with crossed-out triangle = no dry cleaning
    ("What does a clothing label with a circle and the letter P inside mean?", "Dry clean — professional cleaning"),
    ("What does a crossed-out iron symbol on a clothing label mean?", "Do not iron"),
    # Q297: Oxymoron = contradictory words (duplicate)
    ("What is the term for using a word or phrase that contradicts its own meaning?", "Oxymoron"),
    ("What literary device is the opposite of an oxymoron — where two ideas reinforce each other?", "Tautology"),
    # Q298: Kate Hudson's mother = Goldie Hawn (duplicate)
    ("In what film did Goldie Hawn win her Academy Award?", "Cactus Flower (1969) — Best Supporting Actress"),
    ("What is the name of Goldie Hawn's daughter who is also an actress?", "Kate Hudson"),
    # Q299: Paul Revere / tri-corn hat (duplicate)
    ("What is the name of the famous midnight ride partner of Paul Revere?", "William Dawes (and Samuel Prescott)"),
    ("In what city did Paul Revere begin his famous midnight ride?", "Boston (Charlestown), Massachusetts"),
    # Q300: Shuttlecock in badminton (duplicate)
    ("What is the maximum score in a badminton game?", "21 points (best of 3 games)"),
    ("How many feathers are in a traditional badminton shuttlecock?", "16"),
    # Q301: Andrew Johnson purchased Alaska (duplicate)
    ("Who negotiated the purchase of Alaska for the US?", "Secretary of State William H. Seward"),
    ("What is the largest state in the US by area?", "Alaska"),
    # Q302: National animal of Scotland = Unicorn (duplicate)
    ("In what year did Scotland adopt the unicorn as its national animal?", "12th century"),
    ("Scotland and England were formally united in what year?", "1707 (Acts of Union)"),
    # Q303: Georgia last Confederate state to rejoin (duplicate)
    ("Who was the president of the Confederacy during the Civil War?", "Jefferson Davis"),
    ("In what year did the American Civil War end?", "1865"),
    # Q304: Green Monster at Fenway Park (duplicate)
    ("What advertising was once displayed on the Green Monster?", "Various — Citgo sign nearby is iconic"),
    ("What team plays at Fenway Park?", "Boston Red Sox"),
    # Q305: Cycle clothing / pedal (duplicate)
    ("What cycling shoe brand is named after an Italian word for a cycling shoe?", "Bont, or various Italian brands"),
    ("What is the term for the sport of riding bicycles competitively?", "Cycling"),
    # Q306: Pawn can't move backward (duplicate)
    ("What is the only chess piece that captures differently than it moves?", "Pawn"),
    ("In chess, what is it called when a pawn reaches the end of the board?", "Promotion"),
    # Q307: L'Oréal / 'Because you're worth it' (duplicate)
    ("Who first said L'Oréal's 'Because you're worth it' tagline?", "Ilon Specht (a copywriter), performed by actress Joanne Dusseau"),
    ("How many countries does L'Oréal sell its products in?", "Over 150 countries"),
    # Q308: Friday Night Lights / Odessa TX (duplicate)
    ("What streaming service carries the Friday Night Lights TV series?", "Peacock, Amazon Prime Video, and others"),
    ("What real Texas high school is Friday Night Lights based on?", "Permian High School in Odessa, Texas"),
    # Q309: Tripoli = Libya (Marines Hymn)
    ("What is the capital of Libya?", "Tripoli"),
    ("The Marines Hymn mentions 'the shores of Tripoli' — what war is this from?", "First Barbary War (1801-1805)"),
    # Q310: Cotton candy invented by dentist 1904
    ("In what year was cotton candy first introduced to the public?", "1897 (Wharton) or 1904 (World's Fair)"),
    ("What is cotton candy known as in the UK?", "Candy floss"),
    # Q311: King Tut came to power at age 9
    ("At what age did Alexander the Great become King of Macedon?", "20"),
    ("How old was King Tut when he died?", "About 18-19 years old"),
    # Q312: 18-wheeler trailer has 8 wheels
    ("How many wheels total does a standard 18-wheeler have?", "18"),
    ("How many wheels are on the cab (tractor) of an 18-wheeler?", "10"),
    # Q313: AFC Richmond = Ted Lasso fictional team
    ("What league does AFC Richmond compete in on the show Ted Lasso?", "The English Premier League (they rise to the Premier League)"),
    ("What streaming service airs Ted Lasso?", "Apple TV+"),
    # Q314: Knee = largest hinged joint
    ("What is the largest joint in the human body overall (not just hinged)?", "Knee joint"),
    ("What are the two main bones that form the knee joint?", "Femur and tibia (with the patella as the kneecap)"),
    # Q315: Taft = heaviest president at 350+ lbs
    ("What president had a bathtub specially built for him at the White House?", "William Howard Taft"),
    ("After the presidency, what important judicial role did Taft hold?", "Chief Justice of the United States"),
    # Q316: Coffee bean dropped in Sambuca
    ("From what country does Sambuca originate?", "Italy"),
    ("What is the main flavoring agent in Sambuca?", "Anise or elderflower"),
    # Q317: Best killer whale viewing = West Coast
    ("What is another name for the killer whale?", "Orca"),
    ("Are orcas (killer whales) actually whales or dolphins?", "Dolphins (they belong to the dolphin family)"),
    # Q318: Afforestation = planting trees
    ("What is the term for restoring a forest that previously existed?", "Reforestation"),
    ("What is the term for cutting down a forest?", "Deforestation"),
    # Q319: Brooklyn Bridge = oldest over East River
    ("In what year was the Brooklyn Bridge completed?", "1883"),
    ("Who designed the Brooklyn Bridge?", "John Roebling (completed by his son Washington Roebling)"),
    # Q320: 2³ = 8 is highest
    ("What is 2 to the 4th power?", "16"),
    ("What is 3 to the 3rd power (3 cubed)?", "27"),
    # Q321: Vixen = alphabetically last of Santa's reindeer
    ("What is Rudolph the reindeer's distinguishing feature?", "A red glowing nose"),
    ("In what year was the song 'Rudolph the Red-Nosed Reindeer' first recorded?", "1949 (Gene Autry)"),
    # Q322: RSVP = French
    ("What does RSVP stand for in French?", "Répondez s'il vous plaît"),
    ("What does RSVP mean in English?", "Please respond (please reply)"),
    # Q323: Equator resembles latitude
    ("What are the lines running north-south on a globe called?", "Longitude or meridians"),
    ("What is the latitude of the equator?", "0 degrees"),
    # Q324: Thomas Edison was hard of hearing from age 12
    ("What famous invention is Thomas Edison most known for?", "The phonograph and practical incandescent light bulb"),
    ("How many patents did Thomas Edison hold?", "1,093"),
    # Q325: Blepharoplasty = eye surgery
    ("What is rhinoplasty?", "Nose job (surgical reshaping of the nose)"),
    ("What is the medical term for a face lift?", "Rhytidectomy"),
    # Q326: NYC mayor born in Uganda (Zohran Mamdani)
    ("Who is the current mayor of New York City (as of 2026)?", "Zohran Mamdani"),
    ("What political party does NYC Mayor Zohran Mamdani belong to?", "Democratic Party"),
    # Q327: 2 sovereign nations inside Italy = Vatican and San Marino
    ("What is the smallest country in the world by area?", "Vatican City"),
    ("What is the oldest surviving republic in the world?", "San Marino"),
    # Q328: 2 QBs won Super Bowls with 2 teams (Manning and Brady)
    ("Which team did Peyton Manning win his second Super Bowl with?", "Denver Broncos (Super Bowl 50)"),
    ("Which two teams did Tom Brady win Super Bowls with?", "New England Patriots and Tampa Bay Buccaneers"),
    # Q329: End zone = 10 yards past goal line
    ("How wide is an NFL football field from sideline to sideline?", "160 feet (53⅓ yards)"),
    ("How long is an NFL football field including both end zones?", "360 feet (120 yards)"),
    # Q330: Stop signs were yellow before 1954
    ("What color are stop signs in the US today?", "Red"),
    ("In what year did US stop signs become standardized as red?", "1954"),
    # Q331: Kool-Aid Man says 'Oh yeah!'
    ("What does the Kool-Aid Man burst through in commercials?", "Walls"),
    ("What company makes Kool-Aid?", "Kraft Heinz"),
    # Q332: Obie Award for theater
    ("What is the most prestigious award in American professional theater?", "Tony Award"),
    ("The Obie Award recognizes excellence in what type of New York theater?", "Off-Broadway and Off-Off-Broadway theater"),
    # Q333: Lake Champlain borders NY and Vermont
    ("What other state besides New York and Vermont borders Lake Champlain?", "Quebec, Canada (on the northern end)"),
    ("Who discovered Lake Champlain?", "Samuel de Champlain (1609)"),
    # Q334: Joan Francis / Girls Gone Wild (duplicate in S11)
    ("In what decade was Girls Gone Wild at its most popular?", "1990s-2000s"),
    ("What legal trouble did Girls Gone Wild founder Joe Francis face?", "Tax evasion and other charges"),
    # Q335: Bull + man = Minotaur
    ("In what labyrinth was the Minotaur kept?", "The Labyrinth of Crete"),
    ("Who built the labyrinth to house the Minotaur?", "Daedalus"),
    # Q336: Capital of Kuwait = Kuwait City
    ("What sea does Kuwait border?", "Persian Gulf"),
    ("What is Kuwait's main export?", "Oil/petroleum"),
    # Q337: David Copperfield = Dickens' autobiographical novel
    ("What year was David Copperfield published?", "1850"),
    ("Who is the first-person narrator of David Copperfield?", "David Copperfield (himself — it is written in first person)"),
    # Q338: Convex lens bends parallel waves inward
    ("What type of lens is used in a magnifying glass?", "Convex lens"),
    ("What type of lens spreads light rays apart?", "Concave lens"),
    # Q339: 2028 Paralympic Games in Los Angeles
    ("In what year will the 2028 Summer Olympics be held?", "2028"),
    ("In what city are the 2028 Summer Olympics and Paralympics scheduled?", "Los Angeles, California"),
    # Q340: Benjamin Harrison served between Cleveland's two terms
    ("How many consecutive terms did Grover Cleveland serve as president?", "Two non-consecutive terms (22nd and 24th president)"),
    ("In what year was Benjamin Harrison born?", "1833"),
    # Q341: Kingfisher Beer = India
    ("What is the most popular beer brand in India?", "Kingfisher"),
    ("What company brews Kingfisher Beer?", "United Breweries Group"),
    # Q342: Betsy Ross made flag in Philadelphia
    ("Who commissioned Betsy Ross to make the first American flag according to legend?", "George Washington"),
    ("Is the story of Betsy Ross making the first flag historically confirmed?", "No, it is a popular legend but not confirmed"),
    # Q343: Spurs beat OKC Thunder to advance to Finals vs Knicks
    ("What team did the Knicks face in the NBA Finals mentioned in this question?", "San Antonio Spurs"),
    ("What year is this NBA Finals question referring to?", "2025 NBA season"),
    # Q344: Herculaneum destroyed with Pompeii by Vesuvius
    ("In what year did Mount Vesuvius erupt and destroy Pompeii?", "79 AD"),
    ("What city besides Pompeii and Herculaneum was destroyed by Vesuvius in 79 AD?", "Stabiae and Oplontis"),
    # Q345: Nissan sponsors Heisman Trophy
    ("What is the Heisman Trophy awarded for?", "Outstanding college football player of the year"),
    ("In what year was the first Heisman Trophy awarded?", "1935"),
    # Q346: Jennifer Lopez breakout role = Selena (1997)
    ("Who was Selena Quintanilla, the subject of the 1997 film?", "A famous Tejano singer known as the Queen of Tejano"),
    ("What year was Selena Quintanilla murdered?", "1995"),
    # Q347: UFO terrain damage = 2nd kind encounter
    ("What is a first kind encounter with a UFO?", "Visual sighting of a UFO"),
    ("What is a third kind encounter according to the classification system?", "Contact with alien beings"),
    # Q348: Lemon zest = skin of lemon
    ("What kitchen tool is used to create lemon zest?", "Zester or microplane"),
    ("What is the white spongy layer beneath the lemon skin called?", "Pith"),
    # Q349: Ford Model T produced 1908-1927
    ("In what year did Henry Ford introduce the assembly line for the Model T?", "1913"),
    ("How much did the first Ford Model T cost?", "$825 (in 1908); eventually dropped to around $260"),
    # Q350: Dextral = right-handed
    ("What is the opposite of dextral?", "Sinistral (left-handed)"),
    ("Approximately what percentage of humans are right-handed?", "About 85-90%"),
    # Q351: Lennon said Beatles more popular than Jesus
    ("In what year did John Lennon make his famous comment about the Beatles being more popular than Jesus?", "1966"),
    ("What was the public response in the US to Lennon's comment?", "Mass protests, record burnings, radio bans"),
    # Q352: Bad Bunny won Grammy Album of Year 2026
    ("What is the name of Bad Bunny's Grammy-winning album?", "DeBÍ TiRAR MáS FOToS"),
    ("What country is Bad Bunny from?", "Puerto Rico"),
    # Q353: France finished 2nd in FIFA Men's tournament
    ("Who scored the goals for France in the 2026 FIFA World Cup Final?", "Various players (Mbappé among them)"),
    ("In what country was the 2026 FIFA World Cup held?", "USA, Canada, and Mexico"),
    # Q354: Carthage was in modern Tunisia
    ("Who was the most famous general from ancient Carthage?", "Hannibal Barca"),
    ("Carthage was defeated by Rome in what series of wars?", "The Punic Wars"),
    # Q355: People Magazine Sexiest Man Alive 2025 = Jonathan Bailey
    ("What show made Jonathan Bailey famous internationally?", "Bridgerton (Anthony Bridgerton)"),
    ("What nationality is actor Jonathan Bailey?", "British (English)"),
    # Q356: Astros Hall of Famers = Biggio and Bagwell
    ("Craig Biggio played what primary position for the Astros?", "Second baseman (and catcher early in career)"),
    ("Jeff Bagwell played what position for the Houston Astros?", "First baseman"),
    # Q357: OSS = predecessor to CIA
    ("In what year was the CIA (Central Intelligence Agency) established?", "1947"),
    ("What US President created the CIA?", "Harry S. Truman"),
    # Q358: 6x20+9 = 129 (NFL scoring)
    ("In NFL scoring, how many points is a touchdown worth?", "6"),
    ("In NFL scoring, how many points is a field goal worth?", "3"),
    # Q359: Golden State Warriors home = San Francisco (Chase Center)
    ("In what year did the Warriors move to Chase Center in San Francisco?", "2019"),
    ("What arena did the Golden State Warriors play in before Chase Center?", "Oracle Arena in Oakland"),
    # Q360: Dorothy finds Emerald City
    ("In the Wizard of Oz, what is the name of the land where Dorothy lands?", "The Land of Oz"),
    ("Who published the original Wizard of Oz novel?", "L. Frank Baum (published 1900)"),
    # Q361: ROTC R = Reserve
    ("What does ROTC stand for in full?", "Reserve Officers' Training Corps"),
    ("What are the three branches of ROTC in the US?", "Army, Navy (includes Marines), Air Force"),
    # Q362: Pope Leo is a fan of Chicago White Sox
    ("What is Pope Leo XIV's birth name?", "Robert Prevost"),
    ("In what US city was Pope Leo XIV (Robert Prevost) born?", "Chicago, Illinois"),
    # Q363: Texas state reptile = Texas horned lizard
    ("What is the Texas state bird?", "Northern mockingbird"),
    ("What is the Texas horned lizard's defense mechanism?", "Squirting blood from their eyes"),
    # Q364: Saltwater freezes at lower temperature
    ("What is the approximate freezing point of seawater?", "28.4°F (-2°C)"),
    ("Why does saltwater have a lower freezing point than freshwater?", "Salt lowers the freezing point of water (freezing point depression)"),
    # Q365: George Strait's band = Ace in the Hole Band
    ("What genre of country music is George Strait known for?", "Traditional country (honky-tonk)"),
    ("What is George Strait's nickname?", "King of Country"),
    # Q366: Thoroughbred birthday = January 1 (Northern Hemisphere)
    ("Why are all thoroughbred horses given a January 1 birthday?", "To standardize age for racing classifications"),
    ("What are the three races that make up the Triple Crown of horse racing?", "Kentucky Derby, Preakness Stakes, Belmont Stakes"),
    # Q367: Obverse = heads of coin
    ("What is the reverse side of a coin commonly called?", "Tails"),
    ("What term refers to the edge of a coin?", "Rim or edge"),
    # Q368: Johnny Depp played Willie Wonka in 2005
    ("Who played Willie Wonka in the original 1971 film?", "Gene Wilder"),
    ("Who directed the 2005 Charlie and the Chocolate Factory film?", "Tim Burton"),
    # Q369: Coney Island in Brooklyn
    ("What is Coney Island most famous for?", "Amusement parks and beaches"),
    ("What famous hot dog eating contest is held at Coney Island each year?", "Nathan's Famous Hot Dog Eating Contest"),
    # Q370: 2028 Olympics in Los Angeles
    ("In what year were the last Summer Olympics held in Los Angeles before 2028?", "1984"),
    ("How many times has the US hosted the Summer Olympics?", "4 times (1904, 1932, 1984, and upcoming 2028)"),
    # Q371: Bunsen burner invented in Heidelberg
    ("What is a Bunsen burner primarily used for?", "Heating substances in a laboratory"),
    ("What element does a Bunsen burner burn to produce its flame?", "Natural gas or propane"),
    # Q372: 11th Street runs south of Austin Capitol
    ("On what street is the Texas State Capitol located in Austin?", "Congress Avenue"),
    ("In what year was the Texas State Capitol completed?", "1888"),
    # Q373: Bullseye in darts = 50 points
    ("How many points is the outer bull (single bull) worth in darts?", "25 points"),
    ("How many darts does each player throw per turn in standard darts?", "3 darts"),
    # Q374: Silkworms eat mulberry leaves
    ("What material do silkworms produce?", "Silk thread"),
    ("How long is a single thread from one silkworm cocoon?", "About 300-900 meters (up to 1,000 yards)"),
    # Q375: Sloth is not a marsupial (placental)
    ("What is the slowest moving mammal in the world?", "Three-toed sloth"),
    ("How many toes does a three-toed sloth have on each foot?", "3 on back feet, 3 on front limbs"),
    # Q376: Ravens at Tower of London
    ("According to legend, what will happen if the ravens leave the Tower of London?", "The Crown and Tower will fall and Britain will fall"),
    ("How many ravens are kept at the Tower of London by tradition?", "At least 6"),
    # Q377: Rhode Island has largest population among RI, WY, SD, AK
    ("What is the capital of Rhode Island?", "Providence"),
    ("What is Rhode Island's official nickname?", "The Ocean State"),
    # Q378: Mars atmosphere = 96% CO2
    ("What is the atmospheric pressure on Mars compared to Earth?", "About 0.6% of Earth's pressure"),
    ("What makes the Martian sky appear pinkish-red?", "Iron oxide (rust) dust in the atmosphere"),
    # Q379: New Orleans airport named for Louis Armstrong
    ("What is the full name of the New Orleans airport?", "Louis Armstrong New Orleans International Airport"),
    ("In what city was Louis Armstrong born?", "New Orleans, Louisiana"),
    # Q380: Julia Roberts has Oscar (Erin Brockovich 2001)
    ("For what film did Julia Roberts win her Academy Award?", "Erin Brockovich (2001)"),
    ("What was the famous catchphrase or role Julia Roberts played in Pretty Woman (1990)?", "Vivian Ward, a sex worker who falls in love with a wealthy businessman"),
    # Q381: Vicennial = 20 years
    ("What is the term for a 25-year period or anniversary?", "Silver jubilee or sesquicentennial (actually silver jubilee for 25)"),
    ("What is the term for a 50-year anniversary?", "Golden jubilee or semicentennial"),
    # Q382: Nock = notch at end of arrow
    ("What is the feathered end of an arrow called?", "Nock end / fletching end"),
    ("What is the pointed end of an arrow called?", "Arrowhead or tip"),
    # Q383: Theodore Roosevelt = most recent on Mt. Rushmore
    ("Who was the sculptor who carved Mount Rushmore?", "Gutzon Borglum"),
    ("In what state is Mount Rushmore located?", "South Dakota"),
    # Q384: Billie Eilish's brother = Finneas (O'Connell)
    ("What Grammy did Billie Eilish win for her first album?", "All four main Grammy Awards (Record, Album, Song, New Artist) in 2020"),
    ("What is the name of Billie Eilish's debut album?", "When We All Fall Asleep, Where Do We Go?"),
    # Q385: Electric eel native to South America
    ("Is an electric eel actually an eel?", "No — it is a knifefish, not a true eel"),
    ("How many volts can an electric eel generate?", "Up to 860 volts"),
    # Q386: Candyman appears if you say name 5x in mirror
    ("In what year was the original Candyman film released?", "1992"),
    ("What is the Candyman's signature weapon?", "A hook for a hand"),
    # Q387: Unripe cranberries are white
    ("What color do cranberries become when ripe?", "Red"),
    ("In what US state is the most cranberry production concentrated?", "Wisconsin"),
    # Q388: El Paso on Rio Grande
    ("What Mexican city is across the Rio Grande from El Paso?", "Ciudad Juárez"),
    ("In what US state is El Paso located?", "Texas"),
    # Q389: Orient = East, Occident = West
    ("What does the word 'oriental' literally mean?", "Eastern (from Latin oriens, rising sun)"),
    ("What does the term 'occidental' mean?", "Western (from Latin occidens, setting sun)"),
    # Q390: Red + blue = purple
    ("What two colors mix to make orange paint?", "Red and yellow"),
    ("What are the three secondary colors?", "Orange, green, and purple"),
    # Q391: All Quiet on Western Front = WWI
    ("Who wrote All Quiet on the Western Front?", "Erich Maria Remarque"),
    ("In what year was All Quiet on the Western Front published?", "1929"),
    # Q392: Duke is highest rank among Duke, Baron, Count, Marquis
    ("What is the rank directly below Duke in British peerage?", "Marquess (Marquis)"),
    ("What are the five ranks of British peerage in order from highest to lowest?", "Duke, Marquess, Earl, Viscount, Baron"),
    # Q393: Van Buren, Harrison, Hayes were 1800s presidents
    ("What was Martin Van Buren's nickname?", "Old Kinderhook (OK)"),
    ("Who was William Henry Harrison's famous grandson who also became president?", "Benjamin Harrison"),
    # Q394: Philadelphia was US capitol before DC
    ("What is the current capital of Pennsylvania?", "Harrisburg"),
    ("During the Revolutionary War, where did the Continental Congress sometimes meet besides Philadelphia?", "York, Pennsylvania and other cities"),
    # Q395: Die shows 5 on top, 2 on bottom (opposite sides = 7)
    ("What number appears opposite the 1 on a standard die?", "6"),
    ("What number appears opposite the 3 on a standard die?", "4"),
    # Q396: Esmeralda = love interest of Hunchback of Notre Dame
    ("Who is Quasimodo in The Hunchback of Notre Dame?", "The deformed bell-ringer of Notre-Dame cathedral in Paris"),
    ("Who wrote the novel The Hunchback of Notre Dame?", "Victor Hugo"),
    # Q397: Peabody Award = media
    ("In what year were the Peabody Awards first given?", "1941"),
    ("What university oversees and awards the Peabody Awards?", "University of Georgia"),
    # Q398: 'Crazy' by Willie Nelson = trademark of Patsy Cline
    ("In what year did Patsy Cline record her famous version of 'Crazy'?", "1961"),
    ("What was Patsy Cline's real first name?", "Virginia (Virginia Patterson Hensley)"),
    # Q399: Goldilocks first action = eating porridge
    ("In Goldilocks and the Three Bears, how many bowls of porridge did Goldilocks try?", "3 (too hot, too cold, just right)"),
    ("Who wrote the original published version of Goldilocks and the Three Bears?", "Robert Southey (1837)"),
    # Q400: Ryder Cup every 2 years
    ("Who competes in the Ryder Cup?", "Team USA vs Team Europe"),
    ("In what year was the first Ryder Cup competition held?", "1927"),
    # Q401: Jack the Ripper killed in Whitechapel
    ("In what year did Jack the Ripper's murders take place?", "1888"),
    ("How many victims are officially attributed to Jack the Ripper?", "5 canonical victims"),
    # Q402: Iron = Ferrum in Latin (Fe)
    ("What element has the symbol Au on the periodic table?", "Gold"),
    ("What is the Latin word for gold, giving gold its chemical symbol Au?", "Aurum"),
    # Q403: France shares border with Monaco
    ("What sea does Monaco border?", "Mediterranean Sea"),
    ("What is Monaco's primary source of revenue?", "Tourism, gambling, and financial services"),
    # Q404: Swan — cob = male, pen = female
    ("What is a baby swan called?", "Cygnet"),
    ("What is a group of swans in flight called?", "A wedge"),
    # Q405: Fino Sherry = dry
    ("From what country does Sherry wine originate?", "Spain"),
    ("In what Spanish city is Sherry wine (Jerez) primarily produced?", "Jerez de la Frontera"),
    # Q406: Susan B. Anthony = women's suffrage
    ("In what year did US women gain the right to vote?", "1920"),
    ("What constitutional amendment granted women the right to vote in the US?", "19th Amendment"),
    # Q407: 2026 Oscars Best Picture = 'One Battle After Another'
    ("Who directed 'One Battle After Another', the 2026 Oscar Best Picture winner?", "Thomas Friedkin"),
    ("What genre is the film 'One Battle After Another'?", "War drama"),
    # Q408: Forrest Gump attended University of Alabama
    ("What sport did Forrest Gump play at the University of Alabama?", "Football"),
    ("Who played Forrest Gump in the 1994 film?", "Tom Hanks"),
    # Q409: McKinley = 3rd assassinated US president
    ("Who was the 1st US President to be assassinated?", "Abraham Lincoln (1865)"),
    ("Who was the 2nd US President to be assassinated?", "James A. Garfield (1881)"),
    # Q410: Capital of Kentucky = Frankfort
    ("What is the most populous city in Kentucky?", "Louisville"),
    ("What is Kentucky's nickname?", "The Bluegrass State"),
    # Q411: Fort Sill in Oklahoma
    ("What military branch primarily operates Fort Sill?", "US Army"),
    ("What is Fort Sill known for in terms of military function?", "Home of US Army Field Artillery School"),
    # Q412: King Cobra lays eggs
    ("Is the King Cobra the world's longest venomous snake?", "Yes"),
    ("What does a King Cobra eat primarily?", "Other snakes"),
    # Q413: Hawaii state flag has Union Jack
    ("Why does the Hawaii state flag have the Union Jack?", "Hawaii had close ties with Britain; King Kamehameha I used it"),
    ("How many stripes are on the Hawaii state flag?", "8 (representing 8 main islands)"),
    # Q414: Only US state capital on Mississippi = St. Paul (Baton Rouge is not on the main channel)
    ("What river runs through the capital city of Minnesota, St. Paul?", "Mississippi River"),
    ("What is the capital of Minnesota?", "St. Paul"),
    # Q415: Pro boxing round = 3 minutes
    ("How many rounds are in a standard world title boxing match?", "12 rounds"),
    ("How long is the rest period between boxing rounds?", "1 minute"),
    # Q416: Gretel pushed witch in oven
    ("What were the names of the two children in the fairy tale Hansel and Gretel?", "Hansel and Gretel"),
    ("Who collected and published the story of Hansel and Gretel?", "Brothers Grimm"),
    # Q417: W = only letter with more than 1 syllable
    ("How many syllables does the letter M have when spoken?", "1 (em)"),
    ("What letter of the alphabet has three syllables when spoken?", "W (double-u)"),
    # Q418: Snapchat has ghost mascot
    ("What is the name of Snapchat's ghost mascot?", "Ghostface Chillah (or just 'the ghost')"),
    ("In what year was Snapchat founded?", "2011"),
    # Q419: Niagara Falls empties into Lake Ontario
    ("What two bodies of water does Niagara Falls connect?", "Lake Erie (above) and Lake Ontario (below)"),
    ("In what two countries is Niagara Falls located?", "United States and Canada"),
    # Q420: Obie Award = theater (duplicate)
    ("The Obie Award is the oldest theater award in what city?", "New York City"),
    ("What does 'Obie' stand for in the Obie Award?", "Off-Broadway"),
    # Q421: 1,760 yards in a mile
    ("How many feet are in a mile?", "5,280"),
    ("How many inches are in a mile?", "63,360"),
    # Q422: Pikes Peak in Rocky Mountains
    ("How tall is Pikes Peak?", "14,115 feet (4,302 meters)"),
    ("In what US state is Pikes Peak located?", "Colorado"),
    # Q423: Statue of Liberty right hand holds torch
    ("What does the Statue of Liberty hold in her left hand?", "A tablet inscribed with July IV MDCCLXXVI (July 4, 1776)"),
    ("What country gifted the Statue of Liberty to the United States?", "France"),
    # Q424: Beyoncé = Queen B
    ("What is the title of Beyoncé's 2016 visual album?", "Lemonade"),
    ("How many Grammy Awards has Beyoncé won?", "More than 30 (most ever as of 2025)"),
    # Q425: Northern Ireland has 6 counties
    ("What is the capital of Northern Ireland?", "Belfast"),
    ("Northern Ireland is part of what country?", "United Kingdom"),
    # Q426: Torah = Jewish holy book
    ("How many books are in the Torah?", "5 (the Five Books of Moses)"),
    ("What is the first book of the Torah?", "Genesis (Bereshit)"),
    # Q427: Coq au Vin uses red wine
    ("What does 'Coq au Vin' mean in French?", "Rooster in wine"),
    ("What region of France is Coq au Vin most associated with?", "Burgundy (Bourgogne)"),
    # Q428: Michigan = Wolverine State
    ("What is Michigan's state bird?", "American robin"),
    ("What is the University of Michigan's sports team called?", "Wolverines"),
    # Q429: Rubik's Cube has 6 colors
    ("How many individual squares are on a standard Rubik's Cube?", "54 (9 per face × 6 faces)"),
    ("In what country was the Rubik's Cube invented?", "Hungary (by Ernő Rubik)"),
    # Q430: Sandra Bullock born in 1960s (1964)
    ("For what film did Sandra Bullock win her Academy Award?", "The Blind Side (2010)"),
    ("What action-comedy film franchise is Sandra Bullock most associated with?", "Miss Congeniality"),
    # Q431: Malta in Mediterranean Sea
    ("What is the capital of Malta?", "Valletta"),
    ("What is the official language of Malta?", "Maltese and English"),
    # Q432: Odd-numbered pages on right of open book
    ("What is the term for the right-hand page of an open book?", "Recto"),
    ("What is the term for the left-hand page of an open book?", "Verso"),
    # Q433: Friends of Bill W = Alcoholics Anonymous
    ("Who founded Alcoholics Anonymous?", "Bill Wilson (Bill W.) and Dr. Bob Smith"),
    ("In what year was Alcoholics Anonymous founded?", "1935"),
    # Q434: Billie Eilish / Finneas (duplicate in S9)
    ("At what age did Billie Eilish release her debut single 'Ocean Eyes'?", "14"),
    ("What is the name of Billie Eilish's dog?", "Shark"),
    # Q435: Electric eel / South America (duplicate)
    ("Where in South America can electric eels be found?", "Amazon and Orinoco river basins"),
    ("What organ does an electric eel use to generate electricity?", "Electrocytes (specialized cells making up electric organs)"),
    # Q436: Candyman name 5x in mirror (duplicate)
    ("What is the Candyman's backstory?", "He was a freed slave and artist killed by a racist mob"),
    ("A 2021 sequel/spiritual successor to Candyman was directed by whom?", "Nia DaCosta"),
    # Q437: Unripe cranberries white (duplicate)
    ("What is the tart cranberry's official botanical classification?", "Vaccinium macrocarpon"),
    ("What US region is the cranberry most commonly associated with?", "New England (Massachusetts and Wisconsin)"),
    # Q438: El Paso on Rio Grande (duplicate)
    ("El Paso is nicknamed what due to the abundance of sunshine?", "Sun City"),
    ("What mountain range runs through El Paso?", "Franklin Mountains"),
    # Q439: East = Orient, West = Occident (duplicate)
    ("What is the term for countries of East Asia and Southeast Asia collectively?", "The Orient (though this term is now considered outdated)"),
    ("What ocean lies to the east of the Occident (Western countries)?", "Atlantic Ocean"),
    # Q440: Red + blue = purple (duplicate)
    ("What percentage of people are estimated to be unable to see red and green colors properly?", "About 8% of men and 0.5% of women"),
    ("What are the two types of color mixing — one for paint and one for light?", "Subtractive (paint) and additive (light)"),
    # Q441: All Quiet on Western Front = WWI (duplicate)
    ("In what country was Erich Maria Remarque born?", "Germany"),
    ("All Quiet on the Western Front was banned in Nazi Germany in what year?", "1933"),
    # Q442: Duke highest rank (duplicate)
    ("What is the only rank in British peerage above Duke?", "There is none — Duke is the highest rank of British peerage"),
    ("What title does the heir apparent to the British throne typically hold?", "Prince of Wales"),
    # Q443: Van Buren, Harrison, Hayes in 1800s (duplicate)
    ("What year did Rutherford B. Hayes become president?", "1877"),
    ("What was the nickname of William Henry Harrison who served the shortest presidency?", "Tippecanoe"),
    # Q444: Philadelphia was US capitol (duplicate)
    ("In what year did Washington D.C. become the official US capital?", "1800"),
    ("What building was constructed in Philadelphia as the original legislative home?", "Independence Hall"),
    # Q445: Die shows 5 on top, 2 on bottom (duplicate)
    ("On a standard die, what number is opposite the 2?", "5"),
    ("On a standard die, what number is opposite the 6?", "1"),
    # Q446: Esmeralda = Hunchback love interest (duplicate)
    ("In what century was the Hunchback of Notre Dame novel set?", "15th century (1482)"),
    ("Who is the main villain in The Hunchback of Notre Dame?", "Judge Claude Frollo"),
    # Q447: Peabody Award = media (duplicate)
    ("What is the most prestigious award in American journalism?", "Pulitzer Prize"),
    ("The George Foster Peabody Award is named after what type of person?", "An American banker and philanthropist"),
    # Q448: 'Crazy' by Willie Nelson / Patsy Cline (duplicate)
    ("What state was Patsy Cline from?", "Virginia"),
    ("In what year did Patsy Cline die?", "1963 (plane crash)"),
    # Q449: Goldilocks first ate porridge (duplicate)
    ("What chair did Goldilocks break in the three bears' house?", "Baby bear's chair (the little one)"),
    ("In what bed did Goldilocks fall asleep in the three bears' house?", "Baby bear's bed"),
    # Q450: Ryder Cup every 2 years (duplicate)
    ("In what country was the most recent Ryder Cup held?", "Various — held alternately in USA and Europe"),
    ("What is the women's equivalent of the Ryder Cup called?", "Solheim Cup"),
    # Q451: Jack the Ripper Whitechapel (duplicate)
    ("What famous suspect has most often been connected to Jack the Ripper?", "Many suspects — Aaron Kosminski among most cited"),
    ("Was Jack the Ripper ever identified or caught?", "No — the case remains unsolved"),
    # Q452: Iron = Ferrum (duplicate)
    ("What is the symbol for gold on the periodic table?", "Au"),
    ("What element has the symbol Pb, from the Latin plumbum?", "Lead"),
    # Q453: France borders Monaco (duplicate)
    ("What is the population of Monaco?", "About 39,000 (one of the most densely populated countries)"),
    ("Is Monaco a constitutional monarchy?", "Yes"),
    # Q454: Swan — cob male, pen female (duplicate)
    ("What species of swan is native to North America?", "Trumpeter swan and tundra swan"),
    ("How many years can a swan typically live?", "20-30 years in the wild"),
    # Q455: Fino Sherry = dry (duplicate)
    ("What other types of Sherry are there besides Fino?", "Manzanilla, Amontillado, Oloroso, Cream"),
    ("What is the traditional way to serve Fino Sherry?", "Chilled, as an aperitif"),
    # Q456: Susan B. Anthony / women's suffrage (duplicate)
    ("Whose face is on the Susan B. Anthony dollar coin?", "Susan B. Anthony"),
    ("What was Susan B. Anthony arrested for in 1872?", "Voting illegally in a presidential election"),
    # Q457: 2026 Oscar Best Picture (duplicate)
    ("Where is the Academy Awards ceremony typically held?", "Dolby Theatre in Hollywood, Los Angeles"),
    ("In what year were the first Academy Awards held?", "1929"),
    # Q458: Forrest Gump at University of Alabama (duplicate)
    ("What did Tom Hanks say in his acceptance speech referencing Forrest Gump?", "He thanked Forrest Gump's spirit — actually he said nothing Gump-related; he won for Philadelphia and Forrest Gump"),
    ("In the film, what does Forrest Gump say life is like?", "A box of chocolates"),
    # Q459: duck toes facing forward = 3
    ("How many toes does a duck have on each foot in total?", "4 (3 forward-facing plus 1 hind toe)"),
    ("What characteristic feature of duck feet helps them swim?", "Webbing between the toes"),
    # Q460: President 20 years ago Oct 2006 = George W. Bush
    ("What political party did George W. Bush belong to?", "Republican"),
    ("George W. Bush served as governor of which state before becoming president?", "Texas"),
    # Q461: Sierra Nevada majority in California
    ("What is the highest peak in the Sierra Nevada mountain range?", "Mount Whitney"),
    ("Lake Tahoe, a famous Sierra Nevada lake, lies on the border of California and what other state?", "Nevada"),
    # Q462: Hershey PA
    ("What is the name of Hershey's flagship chocolate bar, first sold in 1900?", "Hershey's Milk Chocolate bar"),
    ("Hershey, Pennsylvania was founded in the early 1900s by which chocolate entrepreneur?", "Milton S. Hershey"),
    # Q463: Chimay Beer from Belgium
    ("What type of monks brew Chimay beer in Belgium?", "Trappist monks"),
    ("Belgium is also famous for producing what style of waffles served as street food?", "Brussels waffles (Belgian waffles)"),
    # Q464: Into each life rain must fall = Longfellow
    ("Henry Wadsworth Longfellow wrote 'Paul Revere's Ride' about a midnight rider warning of what event?", "The British were coming (start of the American Revolution)"),
    ("In which Longfellow poem does the line 'Into each life some rain must fall' appear?", "The Rainy Day"),
    # Q465: Amazon Rainforest majority in Brazil
    ("Approximately what percentage of the Amazon Rainforest lies within Brazil?", "About 60%"),
    ("The Amazon River empties into which ocean?", "Atlantic Ocean"),
    # Q466: Milk River Montana
    ("The Milk River flows through Montana and what Canadian province?", "Alberta"),
    ("What is the common name for a liquid produced by cows and used in the Milk River's naming?", "Milk"),
    # Q467: Lincoln (far right on Mt. Rushmore) is Republican
    ("Which US President on Mount Rushmore served just one term?", "Abraham Lincoln (actually served less than two — was assassinated; Theodore Roosevelt served less than two full terms)"),
    ("Mount Rushmore is located in which US state?", "South Dakota"),
    # Q468: Capital of Argentina = Buenos Aires
    ("What does 'Buenos Aires' mean in Spanish?", "Good airs / fair winds"),
    ("Argentina is the world's 8th largest country by area — on what continent?", "South America"),
    # Q469: Sodium Bicarbonate = baking soda
    ("What gas does baking soda produce when mixed with an acid, causing baked goods to rise?", "Carbon dioxide"),
    ("What common household ingredient, when combined with baking soda, creates a cleaning fizz?", "Vinegar"),
    # Q470: Men's Olympic Boxing = 3 rounds
    ("How many minutes is each round in Olympic boxing?", "3 minutes"),
    ("How many weight classes are contested in men's Olympic boxing?", "8 weight classes"),
    # Q471: Largest producer of cork = Portugal
    ("Cork is harvested from the bark of which type of tree?", "Cork oak (Quercus suber)"),
    ("Portugal supplies approximately what fraction of the world's cork?", "About half (around 50%)"),
    # Q472: Chinese checkers max players = 6
    ("What is the minimum number of players needed to play Chinese checkers?", "2"),
    ("Despite the name, Chinese checkers was actually invented in what country?", "Germany"),
    # Q473: NBA MVP on OKC Thunder = Shai Gilgeous-Alexander
    ("What position does Shai Gilgeous-Alexander primarily play?", "Point guard"),
    ("Oklahoma City Thunder play their home games in what arena?", "Paycom Center"),
    # Q474: 1 trillion = 1000 billions
    ("How many millions equal one billion?", "1,000 millions"),
    ("In the long scale used in Europe, one trillion equals how many millions?", "One million millions"),
    # Q475: John Adams and John Quincy Adams
    ("John Quincy Adams was the son of which US President?", "John Adams"),
    ("John Quincy Adams later served in which branch of government after his presidency?", "Congress (US House of Representatives)"),
    # Q476: Austin Powers' occupation = photographer
    ("In Austin Powers, what is the name of Austin's arch-nemesis?", "Dr. Evil"),
    ("Austin Powers is set primarily in what decade when he is first frozen?", "1960s"),
    # Q477: Scorsese first Oscar = The Departed 2007
    ("The Departed was based on a 2002 Hong Kong film with what title?", "Infernal Affairs"),
    ("In The Departed, Jack Nicholson played a crime boss named what?", "Frank Costello"),
    # Q478: Jesus believed to be 33 at death
    ("According to Christian tradition, how many days after his death did Jesus rise?", "3 days"),
    ("What is the term for the event in Christianity celebrating the rising of Jesus?", "Resurrection / Easter"),
    # Q479: Gary Oldman & Ethan Hawke divorced Uma Thurman
    ("In which Quentin Tarantino film did Uma Thurman play Mia Wallace?", "Pulp Fiction"),
    ("Uma Thurman starred in 'Kill Bill' as a character known by what nickname?", "The Bride"),
    # Q480: Rick Perry elected 3 full terms as TX governor
    ("Before serving as Texas Governor, Rick Perry served in what statewide office?", "Lieutenant Governor"),
    ("Rick Perry later served as Secretary of Energy under which US President?", "Donald Trump"),
    # Q481: Official language of Nigeria = English
    ("Nigeria has the largest population of any country in what continent?", "Africa"),
    ("What is the most widely spoken indigenous language in Nigeria?", "Yoruba (or Hausa, or Igbo)"),
    # Q482: Backgammon starting pieces per player = 15
    ("How many points (triangular spaces) are on a backgammon board?", "24"),
    ("In backgammon, what are the two dice-like objects that determine movement?", "Dice"),
    # Q483: Scorpion has 8 legs vs shrimp/crab/lobster 10
    ("To what group of animals do scorpions belong — arachnids or insects?", "Arachnids"),
    ("What sense do scorpions primarily use to detect prey in the dark?", "Vibration/touch (sensing vibrations through hairs and slits)"),
    # Q484: Joan Francis = Girls Gone Wild
    ("Girls Gone Wild was a video brand primarily distributed through which medium in the 1990s?", "Direct TV / late-night infomercials"),
    ("Girls Gone Wild creator Joe Francis was known for operating in what type of entertainment?", "Adult entertainment (risqué videos)"),
    # Q485: Minotaur = man + bull
    ("In Greek mythology, the Minotaur was imprisoned in a labyrinth on what island?", "Crete"),
    ("Who killed the Minotaur in Greek mythology?", "Theseus"),
    # Q486: Capital of Kuwait = Kuwait City
    ("Kuwait City lies on what body of water?", "Arabian Gulf / Persian Gulf"),
    ("Kuwait is bordered to the north and west by which country?", "Iraq"),
    # Q487: David Copperfield is Dickens' autobiographical novel
    ("In David Copperfield, what is the name of the villainous clerk who ruins David's family?", "Uriah Heep"),
    ("Which Charles Dickens novel features the character Fagin leading a gang of pickpockets?", "Oliver Twist"),
    # Q488: Convex lens bends waves inward
    ("What type of lens diverges light rays outward — convex or concave?", "Concave"),
    ("A magnifying glass uses which type of lens — convex or concave?", "Convex"),
    # Q489: 2028 Paralympics = Los Angeles
    ("The Summer Olympics in 2028 will also be held in what city?", "Los Angeles"),
    ("In what year were the Paralympics first held alongside the Olympics in the same city?", "1960 (Rome)"),
    # Q490: Benjamin Harrison served between Cleveland's two terms
    ("Grover Cleveland is the only US President to serve non-consecutive terms — which numbers were his presidencies?", "22nd and 24th"),
    ("Benjamin Harrison was the grandson of which earlier US President?", "William Henry Harrison"),
    # Q491: Kingfisher Beer from India
    ("Kingfisher Beer is headquartered in which Indian city?", "Bangalore (Bengaluru)"),
    ("India's largest state by area is which state?", "Rajasthan"),
    # Q492: Betsy Ross made American flag in Philadelphia
    ("How many stripes are on the American flag?", "13"),
    ("Betsy Ross is said to have made the first American flag at whose request?", "George Washington"),
    # Q493: Spurs defeated OKC in Finals vs Knicks
    ("The San Antonio Spurs are named after which type of cowboy gear?", "Spurs (boot spurs)"),
    ("How many NBA championships did Tim Duncan win with the San Antonio Spurs?", "5"),
    # Q494: Herculaneum destroyed with Pompeii by Vesuvius
    ("In what year did Mount Vesuvius erupt and destroy Pompeii?", "79 AD"),
    ("Pompeii is located near which modern Italian city?", "Naples (Napoli)"),
    # Q495: Heisman sponsor = Nissan
    ("The Heisman Trophy is awarded to the outstanding player in which sport?", "College football"),
    ("The Heisman Trophy is named after John Heisman, who was a pioneer in what sport?", "Football"),
    # Q496: Jennifer Lopez breakout role = Selena (1997)
    ("Selena Quintanilla-Pérez was known as the Queen of what music genre?", "Tejano music"),
    ("Selena was tragically killed in 1995 by the founder of what fan club?", "Selena Fan Club (Yolanda Saldívar)"),
    # Q497: Terrain damaged = 2nd kind UFO encounter
    ("A UFO sighting with no physical evidence is classified as what 'kind' of encounter?", "First kind"),
    ("An encounter with actual extraterrestrial beings is classified as which kind?", "Third kind"),
    # Q498: Skin of lemon = lemon zest
    ("What tool is commonly used to remove lemon zest?", "Microplane/grater or zester"),
    ("What compound in lemon zest gives it its aromatic, citrus flavor?", "Limonene (essential oils)"),
    # Q499: Ford Model T produced 1908-1927
    ("What color did Henry Ford famously say the Model T could be ordered in?", "Any color, so long as it is black"),
    ("On what assembly line principle did Ford revolutionize car manufacturing?", "Moving assembly line / mass production"),
    # Q500: Dextral = right-handed
    ("What is the medical term for a left-handed person?", "Sinistral"),
    ("What percentage of the human population is estimated to be right-handed?", "About 85-90%"),
    # Q501: Lennon quote was about Jesus
    ("In what year did John Lennon make his controversial statement comparing the Beatles to Jesus?", "1966"),
    ("Which US city hosted the first Beatles performance in America in February 1964?", "New York City (Ed Sullivan Show)"),
    # Q502: 2026 Grammys Album of Year = Bad Bunny
    ("Bad Bunny is a singer from which country?", "Puerto Rico"),
    ("What music genre is Bad Bunny primarily associated with?", "Latin trap / reggaeton"),
    # Q503: FIFA 2nd place = France
    ("France won the FIFA World Cup in 1998 — where was that tournament hosted?", "France"),
    ("How many times has France won the FIFA World Cup?", "2 (1998 and 2018)"),
    # Q504: Carthage was in modern Tunisia
    ("What ancient general from Carthage famously crossed the Alps with war elephants?", "Hannibal"),
    ("Carthage was destroyed by Rome at the end of which series of wars?", "Punic Wars"),
    # Q505: People's Sexiest Man Alive 2025 = Jonathan Bailey
    ("Jonathan Bailey rose to fame on which British period drama series?", "Bridgerton"),
    ("People Magazine's Sexiest Man Alive award is given how often?", "Annually"),
    # Q506: Hall of Famers in Astros hat = Biggio/Bagwell
    ("Craig Biggio primarily played what position for the Houston Astros?", "Second baseman"),
    ("Jeff Bagwell won the NL Rookie of the Year in which year?", "1991"),
    # Q507: OSS = predecessor to CIA
    ("What does OSS stand for in the context of WWII intelligence?", "Office of Strategic Services"),
    ("The CIA was established in what year after the OSS was disbanded?", "1947"),
    # Q508: Score calculation question
    ("In what sport is a score called a 'frame'?", "Bowling"),
    ("In American football, how many points does a field goal score?", "3"),
    # Q509: Rotary dial phone = 10 holes
    ("What numbers are on a rotary dial phone?", "0 through 9"),
    ("Rotary dial phones were largely replaced by what type of phone in the 1980s?", "Touch-tone (push-button) phones"),
    # Q510: Fort Knox in Kentucky
    ("What precious metal is stored at Fort Knox?", "Gold"),
    ("Fort Knox is officially known by what name?", "United States Bullion Depository"),
    # Q511: Hillary Clinton's maiden name = Rodham
    ("Hillary Rodham Clinton served as US Secretary of State under which president?", "Barack Obama"),
    ("Hillary Clinton was Senator from which US state?", "New York"),
    # Q512: Halley's Comet = 1P
    ("Approximately how many years does Halley's Comet take to orbit the Sun?", "About 75-76 years"),
    ("When did Halley's Comet last appear visible from Earth?", "1986"),
    # Q513: Victoria Beckham = Posh Spice
    ("Victoria Beckham married which English soccer player?", "David Beckham"),
    ("How many members were in the Spice Girls?", "5"),
    # Q514: Samuel Morse invented Morse Code
    ("What is the Morse Code symbol for the letter SOS?", "... --- ... (three dots, three dashes, three dots)"),
    ("In what year did Samuel Morse send the first electric telegraph message?", "1844"),
    # Q515: Spring begins in March in US
    ("What is the specific date range when spring officially begins in the Northern Hemisphere?", "Around March 19-21 (vernal equinox)"),
    ("What term is used for the first day of spring?", "Vernal equinox"),
    # Q516: Current Pope born in USA = Pope Leo XIV
    ("What was the name of the Pope before Pope Leo XIV?", "Pope Francis"),
    ("In what year was Pope Francis elected as Pope?", "2013"),
    # Q517: Highest number on bingo card = 75
    ("How many numbers are on a standard bingo card (not counting the free space)?", "24 numbers"),
    ("How many columns are on a standard bingo card?", "5"),
    # Q518: Otter lives in a holt
    ("What do you call a group of otters?", "A raft (or bevy)"),
    ("Sea otters famously wrap themselves in what ocean plant to avoid drifting while sleeping?", "Kelp"),
    # Q519: Mayor McCheese has oversized hamburger head
    ("Who is the main clown mascot of McDonald's?", "Ronald McDonald"),
    ("What is the name of the purple blob character from McDonaldland?", "Grimace"),
    # Q520: Santa's reindeer beginning with D = 3 (Dasher, Dancer, Donner)
    ("Name all three of Santa's reindeer whose names begin with the letter D.", "Dasher, Dancer, and Donner"),
    ("Which of Santa's reindeer has a name meaning 'thunder' in German?", "Donner"),
    # Q521: Puerto Rico has more land than Jamaica and Grenada
    ("Puerto Rico is a territory of which country?", "United States"),
    ("Puerto Rico's largest city and capital is?", "San Juan"),
    # Q522: California's slogan = Eureka
    ("What does 'Eureka' mean in Greek?", "I have found it"),
    ("The California Gold Rush began in what year?", "1848"),
    # Q523: Dot over i and j = tittle
    ("What is the name of the dot placed over the letter 'j'?", "Tittle"),
    ("What term describes letters without serifs (small decorative strokes)?", "Sans-serif"),
    # Q524: Mexican town across from Brownsville TX = Matamoros
    ("Matamoros, Mexico is named after a hero of which Mexican war?", "Mexican War of Independence"),
    ("The Rio Grande River forms the border between Brownsville, TX and what Mexican state?", "Tamaulipas"),
    # Q525: First VP to rise to President = John Adams
    ("What term describes a VP who becomes president after the president's death?", "President by succession"),
    ("John Adams was the first vice president under which president?", "George Washington"),
    # Q526: Riesling originated in Germany
    ("In which German wine-growing region did Riesling originate?", "Rhine region (Rhineland)"),
    ("Riesling is primarily characterized as what type of grape — red or white?", "White"),
    # Q527: German Purity Law 1516 = water, hops, barley
    ("The Reinheitsgebot (German Beer Purity Law) was issued in what year?", "1516"),
    ("Which ingredient was added to the German Beer Purity Law in the 19th century as a fourth ingredient?", "Yeast"),
    # Q528: 2025 G20 = South Africa
    ("The G20 is a group of how many major world economies?", "20 (plus the EU)"),
    ("In what city is the African Union headquarters, which has G20 observer status?", "Addis Ababa, Ethiopia"),
    # Q529: Lunker = large fish
    ("What type of fish is most commonly called a 'lunker'?", "Bass (often largemouth bass)"),
    ("In fishing, what term describes catching and immediately releasing a fish?", "Catch and release"),
    # Q530: Joan of Arc burned alive in France
    ("In what year was Joan of Arc burned at the stake?", "1431"),
    ("Joan of Arc was declared a saint by the Catholic Church in what year?", "1920"),
    # Q531: MLK Jr. assassin = James Earl Ray
    ("In what city was Martin Luther King Jr. assassinated?", "Memphis, Tennessee"),
    ("James Earl Ray pled guilty to MLK's murder in what year?", "1969"),
    # Q532: Palermo = capital of Sicily
    ("Sicily is the largest island in which sea?", "Mediterranean Sea"),
    ("Sicily is an autonomous region of which country?", "Italy"),
    # Q533: Scrabble blank tiles = 2
    ("How many total tiles are in a standard English Scrabble set?", "100"),
    ("What is the highest point value for a single tile in Scrabble?", "10 points (Q and Z)"),
    # Q534: Long John Silver was cook on Hispaniola in Treasure Island
    ("Who wrote the novel Treasure Island?", "Robert Louis Stevenson"),
    ("What is the name of the boy narrator in Treasure Island?", "Jim Hawkins"),
    # Q535: Bering Strait separates Alaska from Russia
    ("Approximately how wide is the Bering Strait at its narrowest point?", "About 55 miles (88 km)"),
    ("What two bodies of water does the Bering Strait connect?", "Pacific Ocean and Arctic Ocean"),
    # Q536: Roman chariot race = counterclockwise
    ("How many horses typically pulled a Roman racing chariot called a quadriga?", "4"),
    ("The famous Roman chariot racing track in Rome was called what?", "Circus Maximus"),
    # Q537: Lines parallel to equator = parallels (of latitude)
    ("What do we call the lines that run from pole to pole on a map?", "Meridians (lines of longitude)"),
    ("The equator is at what degree of latitude?", "0 degrees"),
    # Q538: NASA founded 1958 by Eisenhower
    ("NASA stands for what — name all four words?", "National Aeronautics and Space Administration"),
    ("What was the first NASA crewed program, launching in 1958?", "Project Mercury"),
    # Q539: Scrooge saw 4 ghosts total (Marley + 3 spirits)
    ("What are the names of the three Spirits that visit Ebenezer Scrooge?", "Ghost of Christmas Past, Present, and Yet to Come"),
    ("A Christmas Carol was written by which author?", "Charles Dickens"),
    # Q540: Luigi's last name = Mario
    ("In what year did Mario first appear in an arcade game?", "1981 (Donkey Kong)"),
    ("What is Mario's profession in the Nintendo game series?", "Plumber"),
    # Q541: River Spree runs through Berlin
    ("Berlin is the capital of which country?", "Germany"),
    ("What is the name of the famous wall that once divided Berlin?", "Berlin Wall"),
    # Q542: Dak Prescott's middle name = Dakota
    ("Dak Prescott plays quarterback for which NFL team?", "Dallas Cowboys"),
    ("In what college did Dak Prescott play football before the NFL?", "Mississippi State University"),
    # Q543: Most bald eagles in Alaska
    ("The bald eagle is the national symbol of which country?", "United States"),
    ("What is the wingspan of a bald eagle?", "About 6-7.5 feet (1.8-2.3 m)"),
    # Q544: Charlie Brown's father = barber
    ("Who created the Peanuts comic strip?", "Charles M. Schulz"),
    ("In Peanuts, what is the name of Charlie Brown's dog?", "Snoopy"),
    # Q545: Bonspiels in curling
    ("In curling, what is the name of the large stone slid across the ice?", "Rock (or stone)"),
    ("How many players are on a typical curling team?", "4"),
    # Q546: Randalls stores owned by Safeway/Albertsons
    ("Safeway was acquired by which grocery conglomerate in 2015?", "Albertsons"),
    ("In what US state is Safeway's headquarters currently based?", "Idaho (Boise)"),
    # Q547: Betty Ross = love interest of Hulk (Liv Tyler)
    ("What is the alter ego of the Hulk?", "Bruce Banner"),
    ("Liv Tyler played Betty Ross in which Hulk film?", "The Incredible Hulk (2008)"),
    # Q548: BONDYE = supreme god in Voodoo
    ("Voodoo originated primarily in which West African culture?", "Fon and Ewe people of Benin"),
    ("Louisiana Voodoo was influenced by West African traditions brought by whom?", "Enslaved Africans"),
    # Q549: Viridian = shade of green
    ("What mineral is viridian pigment derived from?", "Chromium oxide"),
    ("Name the three primary colors in the traditional color model?", "Red, yellow, and blue"),
    # Q550: Prison currency replaced by ramen noodles
    ("Ramen noodles originated in which country?", "Japan"),
    ("What Japanese soup dish uses a broth with noodles, often confused with ramen?", "Udon or soba"),
    # Q551: Lady Gaga duet 'Die With a Smile' = Bruno Mars
    ("Bruno Mars is from which US state?", "Hawaii"),
    ("What was Bruno Mars' birth name?", "Peter Gene Hernandez"),
    # Q552: Sporran worn by a Scotsman
    ("A sporran is worn over what traditional Scottish garment?", "Kilt"),
    ("What fabric pattern is typically associated with Scottish clans?", "Tartan"),
    # Q553: Appalachian dulcimer = plucked (or strummed)
    ("The Appalachian dulcimer is associated with music from which US region?", "Appalachia (southern Appalachian Mountains)"),
    ("What is the name of the similar European instrument that the dulcimer is related to?", "Zither"),
    # Q554: First credit card = Diners Club 1950
    ("Frank McNamara founded Diners Club after forgetting his wallet at what type of establishment?", "A restaurant"),
    ("What was the first bank-issued general-purpose credit card?", "BankAmericard (later Visa)"),
    # Q555: Joshua Tree National Park = California
    ("Joshua Tree National Park is located at the junction of which two deserts?", "Mojave Desert and Colorado Desert"),
    ("What type of tree gives Joshua Tree National Park its name?", "Joshua tree (Yucca brevifolia)"),
    # Q556: Kids Choice Awards = Nickelodeon
    ("Nickelodeon is owned by which media company?", "Paramount (formerly ViacomCBS)"),
    ("What is the signature gag at the Kids Choice Awards?", "Sliming (green slime)"),
    # Q557: Queen Elizabeth II = Corgi
    ("Queen Elizabeth II reigned for how many years?", "70 years (1952-2022)"),
    ("What is the full breed name of the Queen's preferred Corgi?", "Pembroke Welsh Corgi"),
    # Q558: Male polar bears don't hibernate
    ("Which polar bear gender digs a den and hibernates during winter?", "Female (to give birth)"),
    ("What do polar bears primarily eat?", "Ringed seals (and other seals)"),
    # Q559: 9Lives spokesperson = Morris the cat
    ("What color is Morris the 9Lives cat?", "Orange tabby"),
    ("In what year did Morris the cat first appear in 9Lives commercials?", "1968"),
    # Q560: NCAA Sun Bowl = El Paso, Texas
    ("The Sun Bowl is one of the oldest college football bowl games — in what year was it first played?", "1935"),
    ("El Paso, Texas sits on the border with which Mexican state?", "Chihuahua"),
    # Q561: NA in malt beverages = Non-Alcoholic
    ("What is the typical maximum alcohol content of a non-alcoholic beer?", "0.5% ABV"),
    ("What is the most common type of malt beverage?", "Beer"),
    # Q562: Tower of London was once a prison
    ("Which famous queen was executed at the Tower of London in 1536?", "Anne Boleyn"),
    ("What notorious thieves' operation was associated with the Tower of London's Crown Jewels?", "The 1671 theft attempt by Colonel Blood"),
    # Q563: Q in Q-tip = Quality
    ("Q-tips were invented in the 1920s by which inventor?", "Leo Gerstenzang"),
    ("Q-tips are officially recommended for what use (not ear cleaning)?", "Cosmetic touch-ups and cleaning small areas"),
    # Q564: University of Georgia mascot = Uga
    ("What breed of dog is Uga, the University of Georgia mascot?", "English Bulldog"),
    ("The University of Georgia's sports teams are called by what name?", "Bulldogs"),
    # Q565: Time Athlete of Year and AP Female Athlete 2024 = Caitlin Clark
    ("Caitlin Clark played college basketball at which university?", "University of Iowa"),
    ("Caitlin Clark plays for which WNBA team?", "Indiana Fever"),
    # Q566: Before 1971 New England Patriots = Boston Patriots
    ("What city do the New England Patriots currently play in?", "Foxborough, Massachusetts"),
    ("The New England Patriots have won how many Super Bowl championships?", "6"),
    # Q567: QR = Quick Response
    ("In what country were QR codes invented?", "Japan"),
    ("What company developed QR codes in 1994?", "Denso Wave"),
    # Q568: First African American in Peanuts = Franklin (1968)
    ("Which civil rights figure's letter inspired Charles Schulz to add Franklin to Peanuts?", "Harriet Glickman (a teacher and civil rights activist)"),
    ("In Peanuts, what is the name of the little girl who always pulls the football away from Charlie Brown?", "Lucy van Pelt"),
    # Q569: Salty Dog cocktail = grapefruit juice
    ("What is the difference between a Salty Dog and a Greyhound cocktail?", "A Salty Dog has a salted rim; a Greyhound does not"),
    ("What spirit is used in a Salty Dog cocktail?", "Vodka or gin"),
    # Q570: Utah license plate = The Greatest Snow on Earth
    ("Utah is known for having what type of snow, often cited as ideal for skiing?", "Dry, light powder snow"),
    ("What is the capital city of Utah?", "Salt Lake City"),
    # Q571: Country with X in English name besides Mexico = Luxembourg
    ("What is the capital of Luxembourg?", "Luxembourg City"),
    ("Luxembourg borders which three countries?", "Belgium, France, and Germany"),
    # Q572: X in X-ray = Unknown
    ("Who is credited with discovering X-rays in 1895?", "Wilhelm Röntgen"),
    ("X-rays are a form of what type of radiation?", "Electromagnetic radiation"),
    # Q573: Elysée Palace = France's president
    ("Who currently serves as President of France?", "Emmanuel Macron"),
    ("The Elysée Palace is located in which French city?", "Paris"),
    # Q574: Adult human teeth = 32 (including wisdom teeth)
    ("What are wisdom teeth scientifically called?", "Third molars"),
    ("At what age do wisdom teeth typically emerge?", "17-25 years old"),
    # Q575: Official language of Canary Islands = Spanish
    ("The Canary Islands are an autonomous community of which country?", "Spain"),
    ("What ocean are the Canary Islands located in?", "Atlantic Ocean"),
    # Q576: DuPont created Kevlar
    ("In what decade did DuPont chemist Stephanie Kwolek invent Kevlar?", "1960s (1965)"),
    ("Besides body armor, name one other use of Kevlar.", "Bulletproof vests, cables, fiber optics, tires, racing sails"),
    # Q577: 'Houston we have a problem' = Jim Lovell, Apollo 13
    ("In what year did the Apollo 13 mission take place?", "1970"),
    ("What Oscar-winning film depicts the Apollo 13 crisis?", "Apollo 13 (1995)"),
    # Q578: KKK founded in Tennessee
    ("The KKK was founded in which year?", "1865"),
    ("In which city in Tennessee was the KKK supposedly founded?", "Pulaski"),
    # Q579: Appomattox Court House in Virginia
    ("At Appomattox Court House, who surrendered to General Ulysses S. Grant?", "General Robert E. Lee"),
    ("In what year did the Civil War end at Appomattox?", "1865"),
    # Q580: Waldo wears red and white
    ("Where's Waldo was created by which illustrator?", "Martin Handford"),
    ("What is the British title of the Where's Waldo? book series?", "Where's Wally?"),
    # Q581: Maroon 5 member = Adam Levine, Sexiest Man Alive
    ("In what year was Adam Levine named People's Sexiest Man Alive?", "2013"),
    ("Maroon 5 formed in which US city?", "Los Angeles"),
    # Q582: Chester Cheetah = Cheetos
    ("What company manufactures Cheetos?", "Frito-Lay (PepsiCo)"),
    ("Chester Cheetah's slogan is 'It ain't easy being ___.'", "Cheesy"),
    # Q583: Soccer team rescued from flooded cave in Thailand
    ("What was the name of the youth soccer team rescued from the Thai cave?", "Wild Boars (Moo Pa)"),
    ("The cave rescue in Thailand took place in which year?", "2018"),
    # Q584: SMART car = Swatch + Mercedes
    ("What does SMART stand for in the Smart car brand?", "Swatch Mercedes ART"),
    ("The Smart car is primarily known for being very what?", "Small / compact (city car)"),
    # Q585: Defending FIFA champions = Spain (2026 World Cup)
    ("Spain won the 2026 FIFA World Cup — where was that tournament hosted?", "United States, Canada, and Mexico"),
    ("How many times has Spain previously won the FIFA World Cup before 2026?", "Once (2010)"),
    # Q586: Consumption = tuberculosis
    ("What bacterium causes tuberculosis?", "Mycobacterium tuberculosis"),
    ("The BCG vaccine is used to prevent what disease?", "Tuberculosis"),
    # Q587: Animal judging tortoise and hare race = Fox
    ("Who wrote the original fable of the Tortoise and the Hare?", "Aesop"),
    ("What is the moral lesson of the Tortoise and the Hare fable?", "Slow and steady wins the race"),
    # Q588: Hulk is NOT in Justice League (he's Marvel)
    ("Name three characters who ARE in the Justice League.", "Superman, Batman, Wonder Woman, Flash, Aquaman, Green Lantern, Cyborg"),
    ("The Hulk belongs to which comic book universe?", "Marvel"),
    # Q589: Woodchuck = groundhog
    ("On Groundhog Day, what is the name of the famous groundhog in Punxsutawney, PA?", "Punxsutawney Phil"),
    ("What does it mean if a groundhog sees its shadow on Groundhog Day?", "Six more weeks of winter"),
    # Q590: Theodore Roosevelt said 'Walk softly and carry a big stick'
    ("What does 'walk softly and carry a big stick' mean in diplomacy?", "Speak quietly but be ready to use force"),
    ("Theodore Roosevelt is depicted on which US national monument with other presidents?", "Mount Rushmore"),
    # Q591: Reed Richards = leader of Fantastic Four
    ("What are the superpowers of Reed Richards (Mr. Fantastic)?", "Ability to stretch and elongate his body"),
    ("What villain is the primary enemy of the Fantastic Four?", "Doctor Doom"),
    # Q592: Auld Lang Syne = Days gone by
    ("'Auld Lang Syne' was written by which Scottish poet?", "Robert Burns"),
    ("When is 'Auld Lang Syne' typically sung?", "New Year's Eve / midnight on New Year's"),
    # Q593: Yukon River mouth in Alaska
    ("The Yukon River flows through which two North American countries?", "Canada and the United States"),
    ("What is the approximate length of the Yukon River?", "About 1,980 miles (3,190 km)"),
    # Q594: Glen Powell's call sign in Top Gun: Maverick = Hangman
    ("Who directed Top Gun: Maverick?", "Joseph Kosinski"),
    ("Tom Cruise's call sign in Top Gun is what?", "Maverick"),
    # Q595: Tunisia is in Africa
    ("What is the capital city of Tunisia?", "Tunis"),
    ("Tunisia was the site of what ancient city that rivaled Rome?", "Carthage"),
    # Q596: First African American to win Best Actress = Halle Berry
    ("Halle Berry won her Oscar for Best Actress for which film?", "Monster's Ball"),
    ("In which superhero franchise does Halle Berry play Storm?", "X-Men"),
    # Q597: Nixon first US President to visit China in 1972
    ("Who was China's leader when Nixon made his historic visit in 1972?", "Mao Zedong (and Premier Zhou Enlai)"),
    ("Nixon's visit to China is often described by what phrase?", "Nixon goes to China (opening China to the West)"),
    # Q598: Caution flag in auto racing = yellow
    ("What does a green flag mean in auto racing?", "Start / resume racing"),
    ("What does a black flag mean in auto racing?", "Disqualified / return to pit"),
    # Q599: Black Box on plane = orange
    ("Why is a flight recorder called a 'black box' if it's orange?", "The name predates the switch to orange; 'black box' was a technical slang term"),
    ("What two things does a flight data recorder (black box) record?", "Flight data and cockpit voice recordings"),
    # Q600: Mae West = life jacket
    ("Mae West was a famous actress known for her work in which decade?", "1930s"),
    ("Why was the inflatable life jacket nicknamed a 'Mae West'?", "Because when inflated it resembled Mae West's curvaceous figure"),
    # Q601: Hijacked planes in 9/11 = 4
    ("Where was the fourth hijacked plane on 9/11 headed before it crashed in Pennsylvania?", "Washington D.C. (either the Capitol or White House)"),
    ("The third hijacked plane on 9/11 crashed into what building?", "The Pentagon"),
    # Q602: Monopoly 2nd place beauty contest = $10
    ("How much money do you collect for passing GO in Monopoly?", "$200"),
    ("What is the most expensive property in standard Monopoly?", "Boardwalk"),
    # Q603: Bob Baffert = horse racing
    ("Bob Baffert has trained how many Kentucky Derby winners?", "7"),
    ("What is the name of the famous horse Bob Baffert trained that nearly won the Triple Crown?", "American Pharoah (2015 Triple Crown winner) and Justify (2018)"),
    # Q604: An improper fraction is always greater than 1
    ("What is the definition of an improper fraction?", "A fraction where the numerator is greater than or equal to the denominator"),
    ("Convert the improper fraction 7/4 to a mixed number.", "1 and 3/4"),
    # Q605: Sports with upward counting clock = soccer, Canadian football
    ("In what sport is game time counted down from 60 minutes?", "American football (NFL)"),
    ("Name three sports where the game clock counts up rather than down.", "Soccer, cricket, and Canadian football (others acceptable)"),
    # Q606: Subaru logo = 6 stars (Pleiades)
    ("What Japanese word means 'unite' and gave Subaru its name?", "Subaru (also refers to the Pleiades star cluster in Japanese)"),
    ("The Pleiades star cluster is also known by what common English name?", "The Seven Sisters"),
    # Q607: Sandinistas rule Nicaragua
    ("The Sandinistas take their name from Augusto César Sandino, who fought against whom?", "US occupation of Nicaragua (1920s-1930s)"),
    ("The Sandinistas first took power in Nicaragua in what year?", "1979"),
    # Q608: LP on vinyl album = Long Play
    ("How many minutes of music can a typical LP vinyl record hold per side?", "About 20-25 minutes"),
    ("What does the term '45 RPM' refer to on a vinyl record?", "It rotates at 45 revolutions per minute (single/EP)"),
    # Q609: Fila founded in Italy
    ("In what year was Fila sportswear founded?", "1911"),
    ("Fila is most associated with which sport at the elite level?", "Tennis"),
    # Q610: First Arlington soldiers = Civil War
    ("Who owns and operates Arlington National Cemetery?", "U.S. Army"),
    ("Approximately how many burials take place at Arlington National Cemetery each year?", "About 27 per day / around 7,000 per year"),
    # Q611: Winter Olympics 2026 opening ceremony singer = Mariah Carey
    ("The 2026 Winter Olympics are being held in which two Italian cities?", "Milan and Cortina d'Ampezzo"),
    ("What signature song is Mariah Carey famous for performing at Christmas?", "All I Want for Christmas Is You"),
    # Q612: Carlsberg Beer = Denmark
    ("Carlsberg is named after what?", "The 'Carl's berg' (Carl's hill) where the brewery was built"),
    ("In what year was Carlsberg founded?", "1847"),
    # Q613: World's largest democracy by population = India
    ("India's constitution came into effect in what year?", "1950"),
    ("What is the name of India's parliament?", "Sansad (Parliament of India) — composed of the Rajya Sabha and Lok Sabha"),
    # Q614: Pencil 'lead' = graphite
    ("Graphite used in pencils is a form of which element?", "Carbon"),
    ("Why was graphite originally thought to be a form of lead?", "It looked similar and made dark marks, like lead"),
    # Q615: Yeti cooler brand shares name with legendary ape-like creature
    ("In what US city is Yeti Coolers headquartered?", "Austin, Texas"),
    ("Yeti is a cryptid (mythical creature) said to live in which mountain range?", "Himalayas"),
    # Q616: Grammy = Gramophone
    ("The Grammy Award is named after the gramophone — who is credited with inventing the gramophone?", "Emile Berliner"),
    ("In what year were the first Grammy Awards presented?", "1959"),
    # Q617: Single piece of data = datum
    ("What is the plural of 'datum'?", "Data"),
    ("In statistics, what is a 'data set'?", "A collection of data points or values"),
    # Q618: EU members currently = 27
    ("What was the most recent country to join the European Union?", "Croatia (2013)"),
    ("Which country left the European Union in 2020?", "United Kingdom (Brexit)"),
    # Q619: ACC mascot = Riverbat
    ("Austin Community College is located in which Texas city?", "Austin"),
    ("What type of bat is found along the Colorado River near Austin?", "Mexican free-tailed bat"),
    # Q620: Angle between clock hands at 1:00 = 30 degrees
    ("If the time is 3:00, what is the angle between the hour and minute hands?", "90 degrees"),
    ("How many degrees does the hour hand of a clock move in one hour?", "30 degrees"),
    # Q621: Lake Michigan only Great Lake not bordering Canada
    ("Which is the largest of the Great Lakes by surface area?", "Lake Superior"),
    ("Name all five Great Lakes.", "Superior, Michigan, Huron, Erie, Ontario"),
    # Q622: Terminal velocity = top falling speed
    ("What force causes a falling object to reach terminal velocity?", "Air resistance (drag) balancing gravity"),
    ("Approximately what is the terminal velocity of a skydiver in freefall?", "About 120 mph (195 km/h) in a belly-to-earth position"),
    # Q623: The House that Ruth built = Yankee Stadium
    ("Babe Ruth played for which team before the New York Yankees?", "Boston Red Sox"),
    ("What nickname was given to Babe Ruth?", "The Sultan of Swat / The Bambino"),
    # Q624: Insuperable = difficult to overcome
    ("What is an antonym (opposite) of 'insuperable'?", "Surmountable / possible"),
    ("Use 'insuperable' in a sentence.", "(Accept any correct usage, e.g. 'The obstacle proved insuperable.')"),
    # Q625: I in IED = Improvised
    ("IEDs became notorious during which conflict, where they caused many US casualties?", "Iraq War and Afghanistan War"),
    ("What does the 'E' stand for in IED?", "Explosive"),
    # Q626: Iodine added to salt to prevent goiter
    ("What does the thyroid gland do with iodine?", "Produces thyroid hormones"),
    ("Iodized salt was introduced in the United States in what decade?", "1920s (1924)"),
    # Q627: Paddington Bear named after Paddington Station
    ("Paddington Bear came from which continent in the children's books?", "South America (Peru)"),
    ("Who wrote the Paddington Bear books?", "Michael Bond"),
    # Q628: Spell 'absence' correctly
    ("What is the correct spelling of the word meaning 'not present'?", "A-B-S-E-N-C-E"),
    ("What part of speech is the word 'absence'?", "Noun"),
    # Q629: Only country spanning Asia and Africa = Egypt
    ("What body of water separates the Asian and African parts of Egypt?", "Suez Canal"),
    ("What is the capital of Egypt?", "Cairo"),
    # Q630: National symbol of India since 1950 = tigers
    ("What is the name of the conservation project in India dedicated to protecting tigers?", "Project Tiger"),
    ("Approximately how many Bengal tigers exist in the wild today?", "Around 3,000-3,500"),
    # Q631: Facebook purchased Instagram
    ("In what year did Facebook purchase Instagram?", "2012"),
    ("How much did Facebook pay to acquire Instagram?", "About $1 billion"),
    # Q632: Longfellow poem: village blacksmith under chestnut tree
    ("Henry Wadsworth Longfellow was born in which US state?", "Maine"),
    ("What is the title of Longfellow's famous poem about a midnight rider?", "Paul Revere's Ride"),
    # Q633: Archimedes screw device to raise water
    ("Archimedes' screw is still used today for what purpose?", "Irrigation, sewage treatment, and moving grain"),
    ("Archimedes said 'Give me a lever long enough and a fulcrum... and I shall move the world.' What simple machine was he referring to?", "Lever"),
    # Q634: Warren Buffett = Oracle of Omaha
    ("Warren Buffett is the CEO of which holding company?", "Berkshire Hathaway"),
    ("Warren Buffett is known for his investment philosophy focused on what type of stocks?", "Value investing / undervalued stocks"),
    # Q635: 1 3/4 = 14 eighths
    ("How many sixteenths are in 1 and 3/4?", "28"),
    ("Convert 14/8 to a mixed number in its simplest form.", "1 and 3/4"),
    # Q636: Arizona capital named after mythical bird
    ("What mythical bird rises from its own ashes?", "Phoenix"),
    ("In what year was Phoenix, Arizona founded?", "1867"),
    # Q637: Miley Cyrus first hit = Wrecking Ball
    ("In what year was Wrecking Ball released?", "2013"),
    ("What is the name of Miley Cyrus' Hannah Montana character?", "Miley Stewart / Hannah Montana"),
    # Q638: NASA Curiosity on Mars since 2012
    ("How long does it take to travel from Earth to Mars?", "About 6-9 months (depends on orbital alignment)"),
    ("What is the name of NASA's Mars rover that landed in 2021?", "Perseverance"),
    # Q639: Aquaman = Arthur Joseph Curry
    ("Who plays Aquaman in the DC Extended Universe films?", "Jason Momoa"),
    ("Aquaman's primary superpower is the ability to do what?", "Communicate with and control sea life, and breathe underwater"),
    # Q640: $100 bill shows Philadelphia landmark (Independence Hall)
    ("Whose portrait is on the US $100 bill?", "Benjamin Franklin"),
    ("Independence Hall in Philadelphia was the site of what historic document's signing?", "U.S. Constitution and Declaration of Independence"),
    # Q641: Eisenhower broke off diplomatic relations with Cuba
    ("In what year did Fidel Castro come to power in Cuba?", "1959"),
    ("What famous 1961 failed invasion attempt targeted Cuba?", "Bay of Pigs invasion"),
    # Q642: Current president of France = Macron
    ("Emmanuel Macron was elected President of France in what year?", "2017"),
    ("What political party does Emmanuel Macron lead?", "En Marche! / Renaissance"),
    # Q643: Louvre main entrance = glass pyramid
    ("The glass pyramid at the Louvre was designed by which architect?", "I. M. Pei"),
    ("In what year was the Louvre pyramid completed?", "1989"),
    # Q644: LG TV brand founded in South Korea
    ("What does LG stand for?", "Lucky Goldstar (now 'Life's Good')"),
    ("LG is headquartered in which South Korean city?", "Seoul"),
    # Q645: Muslim holy day = Friday
    ("What is the Islamic prayer service on Friday called?", "Jumu'ah (Friday prayer)"),
    ("What is the Islamic name for the five daily prayers?", "Salah / Salat"),
    # Q646: Horologist = interested in clocks
    ("What is the study of measuring time called?", "Horology"),
    ("The world's most accurate clock is called what type of clock?", "Atomic clock"),
    # Q647: President Taft alive 1857-1930
    ("William Howard Taft was the only person to serve as both President and what other top position?", "Chief Justice of the Supreme Court"),
    ("Taft was known for getting stuck in the White House — in what specific place?", "The bathtub"),
    # Q648: Chef's hat 100 folds = 100 ways to prepare eggs
    ("A chef's tall hat is called by what French name?", "Toque blanche"),
    ("What is the world record for most omelets made in one hour?", "(Accept any reasonable answer — current record exceeds 400)"),
    # Q649: Coney Island in Brooklyn
    ("What is Coney Island's most famous landmark amusement park ride?", "The Cyclone (roller coaster)"),
    ("How many boroughs does New York City have?", "5"),
    # Q650: Dell = small wooded valley
    ("Name another well-known valley in the US that shares 'valley' in its name.", "(Accept: Napa Valley, Silicon Valley, San Fernando Valley, Death Valley, etc.)"),
    ("In the nursery rhyme 'The Farmer in the Dell,' what does 'dell' refer to?", "A small, secluded valley"),
    # Q651: Blue Angels = US Navy (Thunderbirds = Air Force)
    ("How many aircraft are in the main formation of the Blue Angels?", "6"),
    ("The US Air Force's aerial demonstration squadron is called what?", "Thunderbirds"),
    # Q652: Philadelphia Eagles logo faces left
    ("When was the Philadelphia Eagles NFL team founded?", "1933"),
    ("The Eagles play their home games at which stadium?", "Lincoln Financial Field"),
    # Q653: Bed bugs cannot fly
    ("What do bed bugs primarily feed on?", "Blood (human blood)"),
    ("What is the most effective way to kill bed bugs in bedding?", "High heat (washing and drying at high temperature)"),
    # Q654: Subaru discontinuing Legacy
    ("What was the Subaru Legacy's main market segment?", "Mid-size sedan (family car)"),
    ("Name the Subaru model that replaced the Legacy in popularity.", "Subaru Outback (wagon variant)"),
    # Q655: Kellogg's = Michigan
    ("What city in Michigan is home to the Kellogg's headquarters?", "Battle Creek"),
    ("Who founded Kellogg's cereal company?", "W.K. Kellogg (Will Keith Kellogg)"),
    # Q656: Pigs have most nipples (14-16)
    ("How many nipples does a female cat typically have?", "6-8"),
    ("What is the scientific term for a mammal's nipple?", "Nipple or mammary papilla"),
    # Q657: Brunei surrounded by Malaysia
    ("What body of water does Brunei lie on the coast of?", "South China Sea"),
    ("Brunei is a sultanate — what is the sultan known for?", "Being one of the wealthiest people in the world"),
    # Q658: Typical running track = 8 lanes
    ("What is the standard length of one lap around an Olympic running track?", "400 meters"),
    ("In which Olympic event do runners compete in the inside lane for the entire race?", "Marathon (run on roads, not track)"),
    # Q659: Kansas City Chiefs plan to move to Kansas in 2031
    ("In which city and state do the Kansas City Chiefs currently play?", "Kansas City, Missouri"),
    ("How many Super Bowl championships have the Kansas City Chiefs won?", "4 (as of 2024)"),
    # Q660: 4 cm = 40 mm
    ("How many millimeters are in 1 meter?", "1,000 mm"),
    ("How many centimeters are in 1 foot?", "About 30.48 cm"),
    # Q661: Hanukkah = 8 days
    ("What instrument is lit during Hanukkah?", "Menorah (specifically a Hanukkiah with 9 branches)"),
    ("What traditional Hanukkah food is fried in oil to commemorate the miracle?", "Latkes (potato pancakes) and sufganiyot (jelly doughnuts)"),
    # Q662: First stackable potato chip = Pringles
    ("What is the iconic canister shape called that Pringles are sold in?", "Tubular/cylindrical canister"),
    ("What is the saddle shape of a Pringle chip called mathematically?", "Hyperbolic paraboloid"),
    # Q663: Shrimp's heart is in its head
    ("In which part of a shrimp's body are the intestines found?", "The tail"),
    ("What color is shrimp blood?", "Blue (contains hemocyanin, not hemoglobin)"),
    # Q664: Coconut has 3 eyes at base
    ("The three 'eyes' of a coconut are actually what?", "Pores (germination pores)"),
    ("Coconuts are botanically classified as what type of fruit?", "A drupe (stone fruit)"),
    # Q665: Jamestown 1607 = first permanent English settlement
    ("What is the name of the Virginia Indian tribe that lived near Jamestown?", "Powhatan Confederacy"),
    ("In what year did the 400th anniversary of Jamestown take place?", "2007"),
    # Q666: Salubrious = healthy
    ("What is the antonym (opposite) of salubrious?", "Unhealthy, noxious, harmful"),
    ("What Latin root word gives us 'salubrious'?", "Salus (meaning health)"),
    # Q667: Analgesic treats pain
    ("Name a common over-the-counter analgesic.", "Aspirin, ibuprofen, or acetaminophen (Tylenol)"),
    ("What is the difference between an analgesic and an anesthetic?", "Analgesics relieve pain without loss of consciousness; anesthetics block all sensation"),
    # Q668: Michelin Guide max = 3 stars
    ("What does a one-star Michelin rating mean?", "A very good restaurant worth stopping at"),
    ("What nationality is the Michelin Guide, which also makes tires?", "French"),
    # Q669: University of Pennsylvania = Ivy League
    ("How many schools are in the Ivy League?", "8"),
    ("Which Ivy League school is located in New Haven, Connecticut?", "Yale University"),
    # Q670: California Valley Girls = San Fernando Valley
    ("In which US state is the San Fernando Valley located?", "California"),
    ("The 'Valley Girl' accent is associated with which decade?", "1980s"),
    # Q671: M in Roman numerals = 1000
    ("What Roman numeral represents 500?", "D"),
    ("How would you write 1999 in Roman numerals?", "MCMXCIX"),
    # Q672: Chopin wrote music only for piano
    ("Frédéric Chopin was born in which country?", "Poland"),
    ("Chopin spent much of his adult life in which European city?", "Paris"),
    # Q673: Arena football = 8 players per team
    ("How many players per team are on a standard American football field?", "11"),
    ("What is the width of an Arena football field compared to NFL?", "Arena football uses an indoor, smaller field (50 yards wide)"),
    # Q674: Federal minimum wage since 2009 = $7.25
    ("When was the federal minimum wage first established in the US?", "1938"),
    ("What year was the US federal minimum wage last raised?", "2009 (to $7.25)"),
    # Q675: Tincture = soaked in alcohol
    ("What is a common example of a tincture used in medicine?", "Tincture of iodine, or herbal tinctures like echinacea"),
    ("In heraldry, 'tincture' refers to what aspect of a coat of arms?", "The colors and metals used"),
    # Q676: First voice recording = Edison saying Mary Had a Little Lamb
    ("Thomas Edison invented the phonograph in what year?", "1877"),
    ("What material was used on Edison's first phonograph cylinders?", "Tin foil"),
    # Q677: In American Pie, James Dean's coat was borrowed
    ("Don McLean's 'American Pie' refers to the 'day the music died' — what event was this?", "The plane crash that killed Buddy Holly, Ritchie Valens, and The Big Bopper (1959)"),
    ("What year was 'American Pie' released?", "1971"),
    # Q678: Nicki Minaj called JD Vance an assassin
    ("JD Vance served as US Senator from which state?", "Ohio"),
    ("JD Vance served as Vice President under which president?", "Donald Trump"),
    # Q679: 1500 meters = metric mile
    ("1500 meters is how many feet?", "About 4,921 feet"),
    ("What is a standard running mile in meters?", "1,609 meters"),
    # Q680: Tiramisu = 'pick me up' in Italian
    ("What is the main flavor ingredient that provides the 'pick me up' in tiramisu?", "Espresso / coffee"),
    ("What creamy Italian cheese is used in traditional tiramisu?", "Mascarpone"),
    # Q681: Front of skateboard = nose
    ("What is the back end of a skateboard called?", "Tail"),
    ("What is the name of the most basic skateboarding trick where the board flips?", "Ollie"),
    # Q682: Painter of Whistler's Mother was named Whistler
    ("What is the official title of 'Whistler's Mother'?", "Arrangement in Grey and Black No. 1"),
    ("Where is the original painting of Whistler's Mother currently displayed?", "Musée d'Orsay, Paris"),
    # Q683: Spielberg first Oscar = Schindler's List 1994
    ("Schindler's List is based on a novel by which author?", "Thomas Keneally"),
    ("Schindler's List was filmed primarily in black and white — in what year was it released?", "1993"),
    # Q684: Lynyrd Skynyrd named after PE teacher
    ("What famous song did Lynyrd Skynyrd release in 1974 about their Southern identity?", "Sweet Home Alabama"),
    ("Lynyrd Skynyrd tragically lost members in a 1977 plane crash — what was the lead singer's name?", "Ronnie Van Zant"),
    # Q685: Apitoxin = bee venom
    ("What protein in bee venom causes the main allergic reaction in some people?", "Melittin and phospholipase A2"),
    ("Apitherapy is a practice that uses what to treat ailments?", "Bee venom (bee sting therapy)"),
    # Q686: Tetrapod = 4 limbs
    ("Humans are tetrapods — what are the four limbs humans have?", "Two arms and two legs"),
    ("What evolutionary transition led to tetrapods developing from fish?", "Moving from water to land (emergence from aquatic environments)"),
    # Q687: Hamlet's girlfriend = Ophelia
    ("What happens to Ophelia in Hamlet?", "She goes mad and drowns"),
    ("Who wrote Hamlet?", "William Shakespeare"),
    # Q688: Canadian flag leaf = red
    ("How many points does the maple leaf on the Canadian flag have?", "11"),
    ("In what year was the current Canadian flag with the maple leaf adopted?", "1965"),
    # Q689: Pilots call autopilot 'George'
    ("What is the autopilot system in modern aircraft officially called?", "Autopilot or flight management system"),
    ("Which early aviation pioneer is the autopilot 'George' named for?", "No definitive person — the origin of the name is uncertain"),
    # Q690: Sodium Hypochlorite = bleach (washing machine)
    ("What is the household name for sodium hypochlorite?", "Bleach (chlorine bleach)"),
    ("What percentage of sodium hypochlorite is in typical household bleach?", "About 3-8%"),
    # Q691: 4th community card in Texas Hold'em = the turn
    ("What is the 5th and final community card in Texas Hold'em called?", "The river"),
    ("What are the first three community cards dealt together in Texas Hold'em called?", "The flop"),
    # Q692: Lombard St = San Francisco (world's crookedest)
    ("How many turns does the famous crookedest section of Lombard Street have?", "8 turns (hairpin turns)"),
    ("San Francisco is famous for what type of public transit that runs on cables?", "Cable cars"),
    # Q693: Peter Griffin's dog = Brian
    ("What animated show features Peter Griffin and his dog Brian?", "Family Guy"),
    ("Brian Griffin is unique among Family Guy characters in that he drinks what?", "Martinis (he is an intellectual, alcohol-drinking dog)"),
    # Q694: Apollo 17 - Apollo 11 = 6
    ("Apollo 11 landed on the Moon in what year?", "1969"),
    ("Who were the first two astronauts to walk on the Moon?", "Neil Armstrong and Buzz Aldrin"),
    # Q695: Berbers = Africa
    ("The Berbers (Amazigh) are indigenous to which region of Africa?", "North Africa (Morocco, Algeria, Tunisia, Libya, etc.)"),
    ("What language do the Berber people speak?", "Tamazight (Berber languages)"),
    # Q696: Galileo imprisoned for heliocentric view
    ("In what year was Galileo put under house arrest by the Catholic Church?", "1633"),
    ("What astronomical tool did Galileo use to make his famous observations?", "Telescope"),
    # Q697: Car battery = 12 volts
    ("How many cells make up a standard 12-volt car battery?", "6 cells"),
    ("What type of battery is typically used in electric vehicles?", "Lithium-ion battery"),
    # Q698: Equilateral triangle angles = 60 degrees each
    ("How many degrees are in a right angle?", "90 degrees"),
    ("What type of triangle has all three sides of different lengths?", "Scalene triangle"),
    # Q699: Auld Lang Syne = Old Long Since / Times gone by
    ("In what country did the song 'Auld Lang Syne' originate?", "Scotland"),
    ("Who wrote the words to 'Auld Lang Syne'?", "Robert Burns"),
    # Q700: 80% world's almonds from California
    ("What California region is most known for almond production?", "Central Valley (San Joaquin Valley)"),
    ("Are almonds a type of nut or a seed?", "Technically a seed (drupe)"),
    # Q701: Devil vs Johnny in 'Devil Went Down to Georgia'
    ("What instrument does Johnny play in the song?", "Violin (fiddle)"),
    ("Who performed 'The Devil Went Down to Georgia'?", "Charlie Daniels Band"),
    # Q702: Adele's first 2 albums = 19 and 21
    ("What year was Adele's album '25' released?", "2015"),
    ("Adele is from which UK city?", "London (Tottenham)"),
    # Q703: War of the Roses = England
    ("The War of the Roses was fought between which two English royal houses?", "House of Lancaster (red rose) and House of York (white rose)"),
    ("The War of the Roses ended in 1485 with the accession of which king?", "Henry VII (House of Tudor)"),
    # Q704: Nostradamus = French
    ("In what century did Nostradamus live?", "16th century (1503-1566)"),
    ("What is the name of Nostradamus' famous book of prophecies?", "Les Prophéties"),
    # Q705: VP since 1974 lives at Naval Observatory
    ("Who was the first VP to officially reside at the Naval Observatory?", "Walter Mondale"),
    ("The Naval Observatory is the official residence of the VP — what branch does it belong to?", "US Navy"),
    # Q706: NFL team with plant logo = New Orleans Saints
    ("What is the fleur-de-lis a symbol of in French culture?", "Royalty/French monarchy"),
    ("The New Orleans Saints play their home games at which stadium?", "Caesars Superdome"),
    # Q707: Roquefort cheese from sheep's milk
    ("Roquefort cheese is traditionally aged in caves in which French town?", "Roquefort-sur-Soulzon"),
    ("What type of mold gives blue cheeses like Roquefort their distinctive color?", "Penicillium roqueforti"),
    # Q708: NBA shot clock = 24 seconds
    ("In what year was the shot clock introduced to the NBA?", "1954"),
    ("In WNBA basketball, how many seconds is the shot clock?", "24 seconds (same as NBA)"),
    # Q709: Sherlock Holmes = 221B Baker Street
    ("Who created Sherlock Holmes?", "Arthur Conan Doyle"),
    ("What is the name of Sherlock Holmes' faithful companion and assistant?", "Dr. John Watson"),
    # Q710: Milliner = hat maker/seller
    ("What is the origin of the word 'milliner'?", "From Milan, Italy (milaner), a major center of hat-making"),
    ("What hat is associated with the Mad Hatter in Alice in Wonderland?", "Top hat"),
    # Q711: Cliffs of Dover made of chalk
    ("The Cliffs of Dover are located in which English county?", "Kent"),
    ("What strait do the Cliffs of Dover overlook?", "Strait of Dover (English Channel)"),
    # Q712: Boston airport = BOS
    ("What is Boston Logan International Airport's full official name?", "Boston Logan International Airport (Edward Lawrence Logan)"),
    ("Boston is the capital of which US state?", "Massachusetts"),
    # Q713: Michael Phelps won 8 gold medals at 2008 Olympics
    ("How many total Olympic medals did Michael Phelps win in his career?", "28 (23 gold, 3 silver, 2 bronze)"),
    ("Michael Phelps competed in which Olympic sport?", "Swimming"),
    # Q714: Aurora Borealis = Northern Lights
    ("What causes the Aurora Borealis?", "Charged particles from the sun interacting with Earth's magnetic field and atmosphere"),
    ("The Aurora Australis is the Southern equivalent — in what region can it be seen?", "Antarctica, southern South America, and southern Australia/New Zealand"),
    # Q715: Oprah's production company = Harpo Productions (founded 1986)
    ("What does 'Harpo' spell backwards?", "Oprah"),
    ("Oprah Winfrey's talk show ran for how many seasons?", "25 seasons (1986-2011)"),
    # Q716: 3 balls = pawnbroker symbol
    ("What are the three balls in the pawnbroker symbol derived from?", "The coat of arms of the Medici family"),
    ("What does a pawnbroker do?", "Provides loans in exchange for personal property as collateral"),
    # Q717: NHL founded first (1917) vs NFL (1920) and NBA (1946)
    ("In what year was the first Stanley Cup awarded?", "1893"),
    ("How many teams were in the original NHL?", "4 teams"),
    # Q718: Lotus = Buddhist symbol of purity
    ("The lotus flower grows in what type of environment?", "Muddy/murky water"),
    ("In Hinduism, what god is associated with the lotus flower?", "Brahma, Vishnu, or Lakshmi"),
    # Q719: Longest running college football game host = Columbus GA / Philadelphia
    ("What is the name of the oldest college football rivalry game?", "The Game (Harvard vs. Yale) or Lehigh-Lafayette rivalry"),
    ("College football was first played in 1869 between which two universities?", "Rutgers and Princeton"),
    # Q720: Hadrian's Wall = 73 miles, divides England from Scotland
    ("In what century was Hadrian's Wall built?", "2nd century (122 AD)"),
    ("Who ordered the construction of Hadrian's Wall?", "Roman Emperor Hadrian"),
    # Q721: Spider-Man = Marvel/Disney character
    ("What is Spider-Man's real name?", "Peter Parker"),
    ("Spider-Man first appeared in which comic?", "Amazing Fantasy #15 (1962)"),
    # Q722: Star Spangled Banner inspired by War of 1812
    ("Who wrote the poem that became The Star-Spangled Banner?", "Francis Scott Key"),
    ("What specific battle inspired Francis Scott Key to write the poem?", "Battle of Baltimore (bombardment of Fort McHenry)"),
    # Q723: Brooklyn has largest NYC population
    ("What is the most populous borough of New York City?", "Brooklyn"),
    ("In what year did Brooklyn become part of New York City?", "1898"),
    # Q724: Joan of Arc born 1412 = Maid of Orléans
    ("What is the French name for Joan of Arc?", "Jeanne d'Arc"),
    ("Joan of Arc claimed to receive visions from which three saints?", "Saint Michael, Saint Catherine, and Saint Margaret"),
    # Q725: Mars = Red Planet
    ("What gives Mars its reddish color?", "Iron oxide (rust)"),
    ("How many moons does Mars have?", "2 (Phobos and Deimos)"),
    # Q726: Star of David = 6 points
    ("What is the Hebrew name for the Star of David?", "Magen David (Shield of David)"),
    ("On the flag of Israel, what color are the stripes and Star of David?", "Blue"),
    # Q727: 1 kilogram = 1000 grams
    ("How many milligrams are in one gram?", "1,000 milligrams"),
    ("A pound is approximately how many grams?", "About 454 grams"),
    # Q728: 3 to the 4th power = 81
    ("What is 2 to the 10th power?", "1,024"),
    ("What is the square root of 81?", "9"),
    # Q729: Starbucks logo = 2-tailed sea siren
    ("What is the mythological creature in the Starbucks logo?", "Siren (a twin-tailed siren)"),
    ("In what year and city was Starbucks founded?", "1971, Seattle, Washington"),
    # Q730: Cinderella's coach transformed from a pumpkin
    ("What did Cinderella's mice transform into for her carriage?", "Horses"),
    ("In the Disney version of Cinderella, what is the name of the fairy godmother?", "The Fairy Godmother (no specific name in Disney's version)"),
    # Q731: Max bowling ball weight = 16 lbs
    ("How many pins are in a standard bowling setup?", "10 pins"),
    ("What is a perfect score in bowling called?", "A 300 (twelve consecutive strikes)"),
    # Q732: George Washington president 1789-1797
    ("George Washington served as president for how many terms?", "2 terms (8 years)"),
    ("Who was George Washington's Vice President for both terms?", "John Adams"),
    # Q733: Carbon = fundamental building block of life
    ("Why is carbon essential for life?", "Carbon forms the backbone of organic molecules like DNA, proteins, and carbohydrates"),
    ("What is the atomic number of carbon?", "6"),
    # Q734: Three of a kind ranks above 2 pair in poker
    ("What poker hand ranks above three of a kind?", "Straight"),
    ("What is the lowest-ranked poker hand?", "High card"),
    # Q735: Sake base = rice
    ("Sake is often described as a 'rice wine' but technically what kind of beverage is it?", "Fermented rice drink (brewed like beer, not distilled like wine)"),
    ("What is the alcohol content of typical sake?", "About 15-20% ABV"),
    # Q736: Ali Baba phrase = Open Sesame
    ("Ali Baba and the 40 Thieves is a story from which famous collection of tales?", "One Thousand and One Nights (Arabian Nights)"),
    ("What did Ali Baba discover behind the rock opened by 'Open Sesame'?", "A cave full of treasure"),
    # Q737: Julius Caesar murdered on March 15
    ("What is the Latin name for March 15th, known as the day Caesar was killed?", "Ides of March"),
    ("How many senators participated in the assassination of Julius Caesar?", "About 60 senators participated in the conspiracy"),
    # Q738: 4th largest US state by land = Montana
    ("What is the largest US state by land area?", "Alaska"),
    ("What is Montana's nickname?", "Big Sky Country"),
    # Q739: Old Hickory = Andrew Jackson
    ("Andrew Jackson was the how-manyth US President?", "7th"),
    ("What is Andrew Jackson famous for in relation to Native Americans?", "Indian Removal Act (Trail of Tears)"),
    # Q740: Elwood P. Dowd's rabbit = Harvey
    ("Harvey is a 1950 film based on a play by which playwright?", "Mary Chase"),
    ("Who played Elwood P. Dowd in the 1950 film Harvey?", "James Stewart"),
    # Q741: Treaty of Paris 1783 ended Revolutionary War
    ("The Treaty of Paris was signed in 1783 in which city?", "Paris, France"),
    ("The Treaty of Paris recognized what for the United States?", "Independence from Great Britain"),
    # Q742: Socrates drank hemlock
    ("What was Socrates convicted of that led to his death sentence?", "Impiety (corrupting the youth and rejecting city's gods)"),
    ("Who was Socrates' most famous student?", "Plato"),
    # Q743: Texas state tree = Pecan
    ("The pecan is native to which continent?", "North America"),
    ("Pecan is a word derived from which Native American language?", "Algonquian"),
    # Q744: JFK won Pulitzer Prize for Profiles in Courage
    ("Profiles in Courage by JFK won the Pulitzer Prize in what year?", "1957"),
    ("JFK wrote Profiles in Courage about what subject?", "Acts of political bravery by US senators"),
    # Q745: Cocaine from coca leaves
    ("In which continent do coca plants naturally grow?", "South America"),
    ("Which country produces the most cocaine in the world?", "Colombia"),
    # Q746: Incan ruins mainly in Peru
    ("What is the name of the most famous Incan citadel in Peru?", "Machu Picchu"),
    ("The Inca Empire was conquered by which Spanish conquistador?", "Francisco Pizarro"),
    # Q747: Tower of London bird = Raven
    ("According to legend, what will happen if the ravens leave the Tower of London?", "The Crown and the Tower will fall (the kingdom will fall)"),
    ("What is the name of the person who tends the Tower of London ravens?", "Ravenmaster"),
    # Q748: Horned toad squirts blood from eyes
    ("What is the scientific name of the horned toad?", "Phrynosoma (genus of horned lizards)"),
    ("What predators does the blood-squirting defense deter?", "Canids (dogs, wolves, coyotes) because the blood contains distasteful chemicals"),
    # Q749: Scurvy caused by lack of Vitamin C
    ("Scurvy was historically common among which group of people?", "Sailors (on long voyages without fresh produce)"),
    ("What food famously prevented scurvy among British sailors?", "Limes (hence the nickname 'Limeys')"),
    # Q750: Virginia Apgar developed newborn scoring test in 1952
    ("What does the Apgar score measure in newborns?", "Heart rate, breathing, muscle tone, reflexes, and skin color"),
    ("What scores are given in the Apgar test?", "0, 1, or 2 for each of 5 criteria (max 10 total)"),
    # Q751: Frisbee inspired by pie tins from Frisbie Pie Company
    ("Where was the Frisbie Pie Company located?", "Bridgeport, Connecticut"),
    ("In what year was the Frisbee officially trademarked by Wham-O?", "1958"),
    # Q752: Theodore Roosevelt named White House in 1901
    ("What was the White House called before Theodore Roosevelt renamed it?", "The Executive Mansion"),
    ("How many rooms does the White House have?", "132 rooms"),
    # Q753: Tesla advocated AC current
    ("What does AC stand for in AC current?", "Alternating current"),
    ("Thomas Edison advocated for DC current — what does DC stand for?", "Direct current"),
    # Q754: Diamond 4 Cs = cut, carat, clarity, color
    ("What does 'carat' measure in relation to diamonds?", "Weight of the diamond"),
    ("What does 'cut' refer to when evaluating diamonds?", "How well the diamond is cut and shaped, affecting its brilliance"),
    # Q755: Knicks = Knickerbockers
    ("What does 'Knickerbocker' refer to historically?", "An early Dutch settler of New York / a style of loose knee-length trousers"),
    ("The New York Knicks play their home games at which arena?", "Madison Square Garden"),
    # Q756: 9-letter fruit like peach without fuzz = nectarine
    ("Are nectarines and peaches the same species?", "Yes, they are the same species (Prunus persica)"),
    ("What gene makes peaches fuzzy and nectarines smooth?", "A recessive gene for smooth skin"),
    # Q757: Sparkling wine = CO2
    ("What is the traditional method of making champagne called?", "Méthode champenoise (traditional method)"),
    ("Champagne can only be called champagne if it comes from which French region?", "Champagne region (northeastern France)"),
    # Q758: Engelbert Humperdinck wrote opera Hansel and Gretel + pop singer same name
    ("The Hansel and Gretel opera by Humperdinck premiered in what year?", "1893"),
    ("The pop singer Engelbert Humperdinck is known for which 1967 hit?", "Release Me"),
    # Q759: Bob Cratchit = father of Tiny Tim
    ("In A Christmas Carol, what is Scrooge's occupation?", "Money lender / counting-house owner"),
    ("What does Tiny Tim famously say at the end of A Christmas Carol?", "God bless us, every one!"),
    # Q760: Australian currency = dollar
    ("In what year did Australia switch from the pound to the dollar?", "1966"),
    ("The Australian dollar is represented by which symbol?", "A$ or AUD"),
    # Q761: FBI motto = Fidelity, Bravery, Integrity
    ("The FBI was founded in what year?", "1908"),
    ("What does FBI stand for?", "Federal Bureau of Investigation"),
    # Q762: Keith Moon = The Who
    ("Keith Moon was known for his eccentric drumming style and for destroying what?", "Hotel rooms and his drum kits"),
    ("What year did Keith Moon die?", "1978"),
    # Q763: Cricket pitcher = bowler
    ("In cricket, what is the name of the fielder who stands behind the wicket?", "Wicket-keeper"),
    ("How many runs are scored in cricket when the ball is hit over the boundary without bouncing?", "6 runs (a six)"),
    # Q764: McDonald's Hamburger University = Chicago
    ("In what year did McDonald's open its first Hamburger University?", "1961"),
    ("McDonald's global headquarters is in which US city?", "Chicago, Illinois"),
    # Q765: Smallest prime number = 2
    ("What is the only even prime number?", "2"),
    ("What is the next prime number after 2?", "3"),
    # Q766: Remember the Alamo = Battle of San Jacinto
    ("In what Texas city did the Battle of the Alamo take place?", "San Antonio"),
    ("What Mexican general led the forces against the Alamo defenders?", "General Antonio López de Santa Anna"),
    # Q767: Ephelides = freckles
    ("What causes freckles (ephelides) to appear?", "Concentrated areas of melanin pigmentation, often triggered by sun exposure"),
    ("What is the more permanent type of skin marking sometimes confused with freckles?", "Moles (nevi)"),
    # Q768: Largest Central American country = Nicaragua
    ("What is the capital of Nicaragua?", "Managua"),
    ("Nicaragua borders which two countries?", "Honduras (north) and Costa Rica (south)"),
    # Q769: Toronto on Lake Ontario
    ("Lake Ontario is the how-manyth largest of the Great Lakes by area?", "Smallest (5th)"),
    ("What major river flows from Lake Ontario to the Atlantic Ocean?", "St. Lawrence River"),
    # Q770: Saints nicknamed 'AINTS'
    ("The New Orleans Saints won their only Super Bowl in what year?", "2010 (Super Bowl XLIV)"),
    ("What quarterback led the Saints to their Super Bowl victory?", "Drew Brees"),
    # Q771: Manx cat has no tail
    ("Where do Manx cats originate from?", "Isle of Man"),
    ("What genetic mutation causes the taillessness in Manx cats?", "A dominant mutation in the T-box gene"),
    # Q772: C4 = Composition 4
    ("C4 explosive was widely used in which US wars?", "Vietnam War, Iraq War, and Afghanistan War"),
    ("C4 can only be detonated by which combination?", "Both heat AND a detonator/shockwave (not by impact alone)"),
    # Q773: LA to Paris time difference = 9 hours
    ("What time zone is Los Angeles in?", "Pacific Time Zone (PT)"),
    ("Paris, France is in which time zone?", "Central European Time (CET, UTC+1, or UTC+2 in summer)"),
    # Q774: Carson City, Nevada named after Kit Carson
    ("Kit Carson was a famous frontiersman and what type of professional?", "Scout, trapper, and soldier"),
    ("Kit Carson served as a scout in which major US military conflict?", "Mexican-American War and Civil War"),
    # Q775: Majority of Turkey in Asia
    ("What is the capital city of Turkey?", "Ankara"),
    ("The small portion of Turkey in Europe is separated from Asia by which body of water?", "Bosphorus Strait"),
    # Q776: Pied Piper town = Hamelin
    ("The Pied Piper is said to have led what animals away from Hamelin first?", "Rats (with his magical pipe music)"),
    ("The Pied Piper legend is from which country?", "Germany"),
    # Q777: Baby otter = pup
    ("What is the collective noun for a group of otters on land?", "A romp"),
    ("What do otters use to open shellfish when they eat?", "Rocks (they carry and use tools)"),
    # Q778: Victor Wembanyama in NBA
    ("Victor Wembanyama plays for which NBA team?", "San Antonio Spurs"),
    ("What country is Victor Wembanyama from?", "France"),
    # Q779: Carter Panama Canal Zone treaties 1977
    ("The Panama Canal was officially transferred to Panamanian control in what year?", "1999"),
    ("The Panama Canal connects which two oceans?", "Atlantic Ocean and Pacific Ocean"),
    # Q780: Third leg of Triple Crown = Belmont Stakes
    ("What are the three races of the US Triple Crown in order?", "Kentucky Derby, Preakness Stakes, Belmont Stakes"),
    ("The Belmont Stakes is run at what track?", "Belmont Park (in Elmont, New York)"),
    # Q781: Nano = billionth
    ("How many nanometers are in one meter?", "1 billion (10^9)"),
    ("What does the prefix 'micro' mean in terms of measurement?", "One millionth"),
    # Q782: F in SPF = Factor (Sun Protection Factor)
    ("SPF 50 blocks approximately what percentage of UVB rays?", "98%"),
    ("What does UVB stand for in the context of sunscreen?", "Ultraviolet B"),
    # Q783: Tasman Sea = between Australia and New Zealand
    ("What is the length of the Tasman Sea at its widest point?", "About 1,400 miles (2,250 km)"),
    ("The Abel Tasman, who discovered Tasmania and New Zealand, was from which country?", "Netherlands (Dutch)"),
    # Q784: All thoroughbred horses official birthday = January 1
    ("What is the official horse birthday in the Southern Hemisphere?", "August 1 (to align with racing seasons)"),
    ("Why do all thoroughbreds share an official January 1 birthday?", "To simplify age grouping for racing categories"),
    # Q785: Starfish = class Asteroidea
    ("How many arms does a typical starfish have?", "5 (though some have more)"),
    ("What remarkable ability do starfish have if they lose an arm?", "They can regenerate the arm"),
    # Q786: Citizen Kane character = Charles Foster Kane
    ("Citizen Kane is widely considered one of the greatest films ever made — who directed it?", "Orson Welles"),
    ("Charles Foster Kane is loosely based on which real-life media magnate?", "William Randolph Hearst"),
    # Q787: Mistletoe tradition = being kissed
    ("What plant tradition involves being kissed when standing beneath it?", "Mistletoe"),
    ("Viscum album is the scientific name for which plant commonly hung at Christmas?", "Mistletoe"),
    # Q788: CNBC = Consumer News and Business Channel
    ("What network owns CNBC?", "NBCUniversal (Comcast)"),
    ("CNBC focuses primarily on what type of news?", "Financial and business news"),
    # Q789: Indiana Jones first name = Henry
    ("Who wrote the original story for Raiders of the Lost Ark?", "George Lucas (and Philip Kaufman)"),
    ("What ancient artifact does Indiana Jones seek in Raiders of the Lost Ark?", "The Ark of the Covenant"),
    # Q790: NCAA women's softball = 7 innings
    ("How many innings are in an MLB baseball game?", "9 innings"),
    ("What is the term for when a pitcher strikes out all three batters in an inning?", "Immaculate inning"),
    # Q791: Luxor hotel in Las Vegas = pyramid-shaped
    ("The Luxor hotel in Las Vegas is named after the ancient Egyptian city of Luxor — what monument does it replicate?", "The Great Pyramid of Giza"),
    ("What famous beam of light shines from the top of the Luxor hotel?", "The Sky Beam (one of the brightest artificial lights in the world)"),
    # Q792: First Postmaster General = Benjamin Franklin (1775)
    ("In what year was the US Postal Service (USPS) established?", "1775 (Continental Postal System)"),
    ("Benjamin Franklin's face appears on which US coin?", "Half dollar (50 cent piece)"),
    # Q793: Women on Supreme Court (2024) = 4
    ("Who was the first woman to serve on the US Supreme Court?", "Sandra Day O'Connor"),
    ("Name the first Black woman appointed to the US Supreme Court.", "Ketanji Brown Jackson"),
    # Q794: Giant armadillo has most teeth
    ("Giant armadillos are native to which continent?", "South America"),
    ("What is unique about giant armadillos' teeth compared to most mammals?", "They have up to 100 teeth — far more than most mammals"),
    # Q795: Superman's X-ray vision can't penetrate lead
    ("Where was Superman born?", "Planet Krypton"),
    ("What is Superman's weakness?", "Kryptonite"),
    # Q796: Apiary = where bees live
    ("What is the person who keeps bees called?", "Beekeeper or apiarist"),
    ("What is the wax structure where bees store honey called?", "Honeycomb"),
    # Q797: Old Man and the Sea set in Cuba
    ("Who wrote The Old Man and the Sea?", "Ernest Hemingway"),
    ("The Old Man and the Sea won the Pulitzer Prize in what year?", "1953"),
    # Q798: Matterhorn in the Alps
    ("In which two countries does the Matterhorn stand?", "Switzerland and Italy"),
    ("What is the height of the Matterhorn?", "4,478 meters (14,692 feet)"),
    # Q799: Male swan = cob
    ("What is a female swan called?", "Pen"),
    ("What is a baby swan called?", "Cygnet"),
    # Q800: Capital of Canada = Ottawa
    ("Ottawa is located in which Canadian province?", "Ontario"),
    ("What river runs through Ottawa?", "Ottawa River"),
    # Q801: Las Vegas blackjack dealer deals left
    ("In blackjack, what numerical value wins closest to but not exceeding?", "21"),
    ("What does it mean to 'bust' in blackjack?", "To go over 21"),
    # Q802: King Arthur's sword = Excalibur
    ("Where did King Arthur pull the sword from, according to legend?", "A stone (or a lake, depending on the version)"),
    ("Who gave King Arthur the sword Excalibur according to some legends?", "The Lady of the Lake"),
    # Q803: Borg Warner Trophy = Indianapolis 500
    ("In what year was the first Indianapolis 500 held?", "1911"),
    ("What is the Borg-Warner Trophy made of?", "Sterling silver"),
    # Q804: Marianas Trench in Pacific Ocean
    ("How deep is the Marianas Trench?", "About 36,000 feet (11,000 meters) at Challenger Deep"),
    ("What is the deepest point in the Marianas Trench called?", "Challenger Deep"),
    # Q805: MLB team not in US = Toronto Blue Jays
    ("Toronto Blue Jays won the World Series in which two consecutive years?", "1992 and 1993"),
    ("The Toronto Blue Jays play at which stadium?", "Rogers Centre"),
    # Q806: Mock Turtle Soup main ingredient = beef (calf's head)
    ("Mock Turtle Soup was created as a less expensive alternative to what?", "Green sea turtle soup"),
    ("In Alice in Wonderland, what creature tells Alice about his life as a real turtle?", "The Mock Turtle"),
    # Q807: Bill Gates' Microsoft co-founder = Paul Allen
    ("In what year did Bill Gates and Paul Allen found Microsoft?", "1975"),
    ("Paul Allen later became co-owner of which NFL team?", "Seattle Seahawks"),
    # Q808: First TX scratch-off ticket purchaser = Ann Richards
    ("Ann Richards served as Texas Governor in which decade?", "1990s (1991-1995)"),
    ("Texas lottery scratch-off tickets were introduced in what year?", "1992"),
    # Q809: Japanese surrender signed on USS Missouri
    ("In what year did Japan formally surrender to the US?", "1945"),
    ("The USS Missouri is permanently moored as a museum at which US naval base?", "Pearl Harbor, Hawaii"),
    # Q810: Sumo wrestlers throw salt before a match
    ("What is the name of the raised ring sumo wrestlers compete in?", "Dohyo"),
    ("How does a sumo wrestler win a match?", "Force the opponent out of the ring or to touch the ground with anything other than the feet"),
    # Q811: 80 proof whiskey = 40% alcohol
    ("How is proof calculated from percentage in the US system?", "Proof = 2 × alcohol percentage by volume"),
    ("What proof is 100% pure ethanol?", "200 proof"),
    # Q812: US population rank: CA, TX, FL, NY
    ("What is the approximate population of California?", "About 39 million"),
    ("Which US state has seen the fastest population growth in recent decades?", "Texas and Florida"),
    # Q813: Walden Pond in Massachusetts
    ("Henry David Thoreau lived at Walden Pond for how long?", "About 2 years, 2 months, and 2 days"),
    ("What was the name of Thoreau's famous book about his time at Walden Pond?", "Walden"),
    # Q814: Bering Strait = 51 miles separating Asia from North America
    ("The Bering Strait was crossed by a land bridge called what during the Ice Age?", "Beringia (or the Bering Land Bridge)"),
    ("What two bodies of water does the Bering Strait connect?", "Pacific Ocean (via Bering Sea) and Arctic Ocean"),
    # Q815: Eleanor Rigby keeps face in a jar by door
    ("Eleanor Rigby was released by the Beatles in what year?", "1966"),
    ("On which Beatles album does Eleanor Rigby appear?", "Revolver"),
    # Q816: Winklevoss twins sued over Facebook
    ("What 2010 film depicted the founding of Facebook and the Winklevoss lawsuit?", "The Social Network"),
    ("What was the approximate settlement paid to the Winklevoss twins by Facebook?", "About $65 million"),
    # Q817: Prince William's first son = George
    ("What is Prince George's full name?", "George Alexander Louis"),
    ("Who is Prince George's mother?", "Princess Catherine (formerly Catherine Middleton)"),
    # Q818: Crystal City, TX = Spinach Capital of the World
    ("What famous cartoon character is associated with spinach and Crystal City, TX?", "Popeye"),
    ("Crystal City erected its Popeye statue in what year?", "1937"),
    # Q819: Smallest Euro banknote = 5 euros
    ("The euro became the official currency of the eurozone in what year?", "1999 (as electronic currency) and 2002 (as cash)"),
    ("What symbol represents the euro?", "€"),
    # Q820: Both Koreas use 'Won' currency
    ("The South Korean Won is represented by which symbol?", "₩"),
    ("The North Korean Won is issued by which governmental institution?", "Central Bank of the Democratic People's Republic of Korea"),
    # Q821: Sega created Sonic the Hedgehog
    ("In what year did Sonic the Hedgehog first appear?", "1991"),
    ("What is Sonic the Hedgehog's special ability?", "Running at supersonic speed"),
    # Q822: Ricin made from castor beans
    ("What country infamously used ricin in the assassination of Georgi Markov in 1978?", "Bulgaria (Soviet-era intelligence)"),
    ("What makes ricin so dangerous?", "It is extremely toxic even in tiny amounts; there is no antidote"),
    # Q823: 2025 Oscar Best Picture = Anora
    ("Who directed the 2025 Best Picture winner Anora?", "Sean Baker"),
    ("Anora is a coming-of-age story set primarily in which US city?", "New York City"),
    # Q824: US flag in 1950 had 48 stars
    ("Which two states were added to the US flag to bring it to 50 stars?", "Alaska and Hawaii (both in 1959)"),
    ("How many stripes are on the US flag?", "13"),
    # Q825: Time Person of Year = Obama, Trump, and Biden all won
    ("Time Person of the Year was awarded to a machine for the first time in what year?", "1982 (the personal computer)"),
    ("Who was the first woman to be named Time Person of the Year?", "Wallis Simpson (1936)"),
    # Q826: 120% as fraction = 6/5
    ("Simplify the fraction 120/100 to its lowest terms.", "6/5"),
    ("What is 6/5 as a decimal?", "1.2"),
    # Q827: Titanic survivors rescued by RMS Carpathia
    ("How many survivors were rescued by the RMS Carpathia?", "About 710 people"),
    ("The Titanic sank in what year?", "1912"),
    # Q828: Ozzy Osbourne real name = John (John Michael Osbourne)
    ("What band was Ozzy Osbourne a founding member of?", "Black Sabbath"),
    ("Ozzy Osbourne became famous for biting the head off what animal during a concert?", "A bat"),
    # Q829: Theodore Roosevelt became president after McKinley assassinated in 1901
    ("William McKinley was assassinated in which US city?", "Buffalo, New York"),
    ("Theodore Roosevelt became the youngest president at what age?", "42 years old"),
    # Q830: John Lennon's murderer = Mark David Chapman
    ("John Lennon was shot outside which famous New York building?", "The Dakota (apartment building)"),
    ("In what year was John Lennon murdered?", "1980"),
    # Q831: Pennsylvania named for William Penn (Quaker), not John Penn
    ("Who founded the Pennsylvania colony?", "William Penn"),
    ("The Quakers are formally known by what name?", "Religious Society of Friends"),
    # Q832: Soporific drug makes you sleepy
    ("Name a common soporific drug used as a sleep aid.", "Diphenhydramine (Benadryl), melatonin, or zolpidem (Ambien)"),
    ("What is the opposite of soporific in medical terms?", "Stimulant"),
    # Q833: Typical crab = 5 pairs (10 legs)
    ("What order do crabs belong to in the animal kingdom?", "Decapoda"),
    ("What are the large front claws of a crab called?", "Chelipeds (or claws/pincers)"),
    # Q834: Canary Islands named after dogs (Canaria)
    ("Where are the Canary Islands located geographically?", "Off the northwest coast of Africa (near Morocco)"),
    ("The word 'canary' for the bird actually comes from the Canary Islands — not the other way around — true or false?", "True"),
    # Q835: Aardvark native to Africa
    ("What does the name 'aardvark' mean in Afrikaans?", "Earth pig"),
    ("What do aardvarks primarily eat?", "Ants and termites"),
    # Q836: US Space Program between Mercury and Apollo = Gemini
    ("The Gemini program was named after the zodiac sign — how many stars make up the twins?", "2 (Castor and Pollux)"),
    ("What was the goal of the Gemini program?", "To develop space travel techniques for the Apollo Moon missions"),
    # Q837: Mini uses slogan 'Be Iconic'
    ("The Mini car brand is currently owned by which company?", "BMW Group"),
    ("The original Mini was designed by which British engineer?", "Alec Issigonis"),
    # Q838: Dizzy Gillespie played trumpet
    ("Dizzy Gillespie helped develop which jazz style in the 1940s?", "Bebop"),
    ("What was Dizzy Gillespie's trademark physical feature while playing trumpet?", "His cheeks puffed out enormously"),
    # Q839: Lucky Charms hearts = pink/red
    ("How many different marshmallow shapes are in Lucky Charms?", "8 (currently — it changes over time)"),
    ("Lucky Charms cereal is made by which company?", "General Mills"),
    # Q840: Levi's logo = two horses demonstrating strength
    ("In what year was Levi Strauss & Co. founded?", "1853"),
    ("What city is Levi's headquartered in?", "San Francisco, California"),
    # Q841: Tour de France overall leader = yellow jersey
    ("What color jersey does the best sprinter wear in the Tour de France?", "Green jersey"),
    ("What color jersey does the best climber wear in the Tour de France?", "Polka dot (white with red dots)"),
    # Q842: Hawaii major islands = 8
    ("What is the largest island in Hawaii?", "Hawaii (the Big Island)"),
    ("What is the capital of Hawaii?", "Honolulu"),
    # Q843: US President's helicopter = Marine One
    ("What is the US President's official airplane called?", "Air Force One"),
    ("What is the callsign of the US Vice President's helicopter?", "Marine Two"),
    # Q844: Microsoft #1 in 2025 by profit/market value
    ("What is Microsoft's most profitable product line or service?", "Cloud computing (Azure) and business software (Office 365)"),
    ("Who founded Microsoft with Bill Gates?", "Paul Allen"),
    # Q845: Obama = 44th president
    ("Barack Obama was the first African American to hold what office?", "President of the United States"),
    ("In what state was Barack Obama born?", "Hawaii"),
    # Q846: Motorola created first handheld cell phone in 1973
    ("What was the name of Motorola's first handheld cell phone?", "Motorola DynaTAC 8000X"),
    ("In what year was the first cell phone call made?", "1973"),
    # Q847: Hemisphere = half of a sphere (10 letters)
    ("How many hemispheres is the Earth divided into?", "4 (Northern, Southern, Eastern, Western)"),
    ("What is the other proper 10-letter word for the imaginary line dividing Earth in half?", "Equatorial (or the equator itself)"),
    # Q848: Cristiano Ronaldo highest paid athlete in 2025
    ("For which Saudi Arabian club does Cristiano Ronaldo play?", "Al-Nassr"),
    ("How many Ballon d'Or awards has Cristiano Ronaldo won?", "5"),
    # Q849: Vanderbilt University = Nashville, Tennessee
    ("Vanderbilt University was founded with a donation from which railroad magnate?", "Cornelius Vanderbilt"),
    ("Nashville is also known as what city due to its music industry?", "Music City"),
    # Q850: Heptad = 7 objects
    ("What do you call a group of 8 objects?", "Octad or octet"),
    ("A group of 10 objects is called what?", "Decade or decad"),
    # Q851: Cricket's ears on its legs
    ("What organ do crickets use on their legs to hear?", "Tympanal organ (membrane on the foreleg)"),
    ("Male crickets make chirping sounds using which body part?", "Wings (by rubbing them together — stridulation)"),
    # Q852: Baccarat player gets 2 cards
    ("In baccarat, a hand totaling more than 9 is counted how?", "By dropping the tens digit (e.g., 14 becomes 4)"),
    ("What does 'baccarat' mean in French/Italian?", "Zero (the value of face cards)"),
    # Q853: Helio = the Sun
    ("What is the study of the Sun called?", "Heliophysics or solar physics"),
    ("What is the name of the boundary of the Sun's influence on surrounding space?", "Heliopause"),
    # Q854: Vermillion = shade of red
    ("Vermillion is derived from what mineral?", "Cinnabar (mercury sulfide)"),
    ("Artists once prized vermillion for its vivid red — what dangerous metal is in cinnabar?", "Mercury"),
    # Q855: Thursday named for Norse Thunder God (Thor)
    ("Which day of the week is named after the Norse god Odin (Woden)?", "Wednesday"),
    ("Which day of the week is named after the planet Saturn?", "Saturday"),
    # Q856: Hepatic = liver
    ("What is the medical term for liver disease?", "Hepatitis (inflammation) or cirrhosis (scarring)"),
    ("The liver produces what substance that helps digest fats?", "Bile"),
    # Q857: Largest mammal in North America = American bison
    ("How many American bison existed before European colonization?", "An estimated 30-60 million"),
    ("Where can you see wild bison in the US today?", "Yellowstone National Park and other preserves"),
    # Q858: Braille total dots = 6
    ("Who invented the Braille system?", "Louis Braille"),
    ("How many possible characters can be created with 6 Braille dots?", "64 combinations"),
    # Q859: Malachite = green
    ("Malachite is often used in what type of decorative art?", "Jewelry, carvings, and decorative objects"),
    ("What metal is malachite a carbonate ore of?", "Copper"),
    # Q860: Lepus = hares
    ("The constellation Lepus (the Hare) lies just below which constellation?", "Orion"),
    ("What is the difference between a hare and a rabbit?", "Hares are larger, faster, and born with open eyes and fur; rabbits are born blind and hairless"),
    # Q861: Caber = log tossed in Highland Games
    ("What is the goal when tossing a caber in the Highland Games?", "To turn it end-over-end so it lands closest to 12 o'clock position"),
    ("The Highland Games originated in which country?", "Scotland"),
    # Q862: Russian astronaut = cosmonaut
    ("What is the Chinese equivalent of an astronaut called?", "Taikonaut"),
    ("The first cosmonaut in space was whom?", "Yuri Gagarin (1961)"),
    # Q863: Tercentenary = 300 years
    ("What is the term for a 250th anniversary?", "Sestercentennial or quarter-millennial"),
    ("What is the term for a 500th anniversary?", "Quincentennial"),
    # Q864: Most recent VP elected President (besides Biden) = George H.W. Bush
    ("George H.W. Bush served as VP under which president?", "Ronald Reagan"),
    ("George H.W. Bush served as president from what year to what year?", "1989-1993"),
    # Q865: Mandarin more widely spoken in China
    ("Approximately how many native speakers does Mandarin Chinese have globally?", "About 920 million"),
    ("What is the most widely spoken dialect of Chinese in Hong Kong?", "Cantonese"),
    # Q866: Ant venom = formic acid
    ("What is the scientific name for an ant colony?", "Formicary"),
    ("What gives fire ants their painful sting?", "Venom called solenopsin (an alkaloid)"),
    # Q867: Diastema = gap between teeth
    ("What famous fashion model is known for her diastema (tooth gap)?", "Lauren Hutton or Lara Stone (accept any)"),
    ("Diastema can be caused by what in children?", "A large labial frenum, thumb-sucking, or tooth/jaw size discrepancy"),
    # Q868: Dipsomaniac = enjoys/addicted to alcohol
    ("What is the medical term for alcoholism?", "Alcohol use disorder (AUD)"),
    ("Dipsomania specifically refers to what pattern of drinking?", "Compulsive periodic binge drinking"),
    # Q869: Orzo = pasta
    ("What does 'orzo' mean in Italian?", "Barley (though orzo is actually pasta made to look like barley/rice)"),
    ("What shape is orzo pasta?", "Small oval/rice-shaped"),
    # Q870: Mojito = 'something a little wet' in Spanish
    ("What are the five classic ingredients of a mojito?", "White rum, lime juice, sugar, mint, and soda water"),
    ("Mojitos originated in which country?", "Cuba"),
    # Q871: Mach = relative to speed of sound
    ("What is the speed of sound at sea level?", "About 767 mph (1,235 km/h) or Mach 1"),
    ("A supersonic aircraft travels at speeds above what Mach number?", "Mach 1"),
    # Q872: Perique tobacco = smoke
    ("Perique tobacco is grown in which US state?", "Louisiana"),
    ("Perique is considered one of the rarest tobaccos — what makes it unique?", "Fermented under pressure, giving it a fruity, spicy flavor"),
    # Q873: Adobe PDF P = Portable
    ("PDF stands for what three words?", "Portable Document Format"),
    ("Adobe PDF was invented by which company and in what year?", "Adobe Systems, 1993"),
    # Q874: UFC main event round = 5 minutes
    ("In UFC, how many rounds are typically in a non-title fight?", "3 rounds"),
    ("What does UFC stand for?", "Ultimate Fighting Championship"),
    # Q875: Bubonic plague spread by fleas
    ("What animal carried the fleas that spread the Black Death (bubonic plague)?", "Rats (primarily black rats)"),
    ("Approximately what percentage of Europe's population died in the Black Death?", "About one-third (30-60%)"),
    # Q876: Bohemian Rhapsody mentions Galileo multiple times
    ("Bohemian Rhapsody was performed by which band?", "Queen"),
    ("In what year was Bohemian Rhapsody released?", "1975"),
    # Q877: Pillywink torture = fingers/thumbs
    ("Pillywinks (pillwinks) were used as a torture device during which historical period?", "Medieval period (Middle Ages)"),
    ("What was the medieval torture device called that crushed fingers?", "Thumbscrew (or pillywinks)"),
    # Q878: 100 Years War = England and France
    ("The Hundred Years' War lasted from approximately what years?", "1337 to 1453"),
    ("What French heroine helped turn the tide of the Hundred Years' War?", "Joan of Arc"),
    # Q879: Myosis = affects sight
    ("What does myosis specifically refer to in medical terms?", "Constriction of the pupil"),
    ("What is the opposite of myosis — dilation of the pupil?", "Mydriasis"),
    # Q880: Lotus = shared by software, vehicle, and Egyptian national flower
    ("Lotus Software was famous for creating which spreadsheet program?", "Lotus 1-2-3"),
    ("The Lotus car company is headquartered in which country?", "United Kingdom (England)"),
    # Q881: MPEG E = Experts
    ("MPEG stands for what?", "Moving Picture Experts Group"),
    ("What common video format does MPEG produce?", ".mpeg or .mp4 files"),
    # Q882: Suez Canal 45 years older than Panama Canal
    ("In what year was the Suez Canal completed?", "1869"),
    ("In what year was the Panama Canal completed?", "1914"),
    # Q883: Grammys Song of the Year 'Luther' = Kendrick Lamar and SZA
    ("'Luther' samples which 1980s R&B singer?", "Luther Vandross"),
    ("Kendrick Lamar won his Grammy for 'Luther' at which Grammy ceremony?", "2025 Grammy Awards (67th)"),
    # Q884: Lowest belt in martial arts = white
    ("What color belt typically indicates the highest rank in many martial arts?", "Black belt"),
    ("How many degrees/dans exist above black belt in many martial arts?", "Up to 10 dan (degrees)"),
    # Q885: FedEx = purple promise
    ("FedEx is short for what full company name?", "Federal Express"),
    ("In what year was FedEx founded?", "1971"),
    # Q886: Snow White dwarves ending in Y = 6 (Grumpy, Sleepy, Bashful, Happy, Dopey, Sneezy)
    ("Name all 7 of Snow White's dwarves.", "Doc, Grumpy, Happy, Sleepy, Bashful, Sneezy, Dopey"),
    ("Which dwarf does NOT have a name ending in Y?", "Doc"),
    # Q887: Friar Tuck = spiritual leader of Robin Hood's band
    ("What is the name of Robin Hood's archery-skilled companion?", "Little John"),
    ("Robin Hood lived in what famous English forest?", "Sherwood Forest"),
    # Q888: Citius Altius Fortius = Faster Higher Stronger
    ("Citius Altius Fortius is the motto of which major sporting event?", "Olympic Games"),
    ("In what year was Citius Altius Fortius adopted as the Olympic motto?", "1894"),
    # Q889: Pillsbury Doughboy = Poppin' Fresh
    ("In what year did Poppin' Fresh (the Pillsbury Doughboy) make his first appearance?", "1965"),
    ("What sound does the Pillsbury Doughboy make when poked in the belly?", "Hee hee (giggle)"),
    # Q890: Crabs molt
    ("What is the process called when a crab sheds its shell?", "Molting (ecdysis)"),
    ("What do crabs do immediately after molting their shell?", "Wait for their new soft shell to harden"),
    # Q891: Grand Slam in golf = 4 tournaments
    ("Name all four golf major championships.", "The Masters, US Open, The Open Championship (British Open), PGA Championship"),
    ("The Masters golf tournament is held at which famous course?", "Augusta National Golf Club"),
    # Q892: Largest hot air balloon festival = Albuquerque, NM
    ("What is the name of the balloon festival in Albuquerque, New Mexico?", "Albuquerque International Balloon Fiesta"),
    ("How many balloons typically participate in the Albuquerque Balloon Fiesta?", "About 500-600 balloons"),
    # Q893: Sidecar = passenger vehicle on motorcycle + cocktail
    ("What are the three ingredients in a classic Sidecar cocktail?", "Cognac, Cointreau (orange liqueur), and lemon juice"),
    ("What glass is a Sidecar cocktail traditionally served in?", "Coupe or martini glass (often with a sugared rim)"),
    # Q894: Roger Federer = Swiss
    ("How many Grand Slam titles did Roger Federer win?", "20"),
    ("Roger Federer is most associated with which Grand Slam tournament?", "Wimbledon (8 titles)"),
    # Q895: Chess queen = most freedom of movement
    ("How many squares can a queen move in a single turn in chess?", "Unlimited squares (any direction)"),
    ("Which chess piece can jump over other pieces?", "The knight"),
    # Q896: Georgy Porgy kissed girls and made them cry
    ("Georgy Porgy is a nursery rhyme — what did Georgy Porgy run from?", "The boys (who came out to play)"),
    ("What is a common theory about the real person behind Georgy Porgy?", "King George IV (or George Villiers, Duke of Buckingham)"),
    # Q897: Don Quixote's sidekick = Sancho Panza
    ("Don Quixote was written by which Spanish author?", "Miguel de Cervantes"),
    ("What does Don Quixote famously tilt at, mistaking them for giants?", "Windmills"),
    # Q898: Boxing Day = December 26
    ("What is Boxing Day and how is it celebrated?", "A public holiday on December 26, traditionally for giving gifts to the less fortunate / servants"),
    ("Boxing Day is primarily observed in which type of countries?", "Commonwealth countries (UK, Canada, Australia, etc.)"),
    # Q899: Double-6 domino set = 28 pieces
    ("How many pips (dots) are on the double-6 domino tile?", "12 (6 on each half)"),
    ("What is the blank domino in a double-6 set called?", "The blank or zero tile"),
    # Q900: Millennium = 1,000 years
    ("What is the term for a 100-year period?", "Century"),
    ("What is the term for a 10-year period?", "Decade"),
    # Q901: Sweet Georgia Brown = Harlem Globetrotters
    ("The Harlem Globetrotters are known for playing basketball combined with what?", "Comedy and entertainment tricks"),
    ("The Harlem Globetrotters were founded in which year?", "1926"),
    # Q902: Peter Parker sold photos to The Daily Bugle
    ("Who is the editor of The Daily Bugle in Spider-Man?", "J. Jonah Jameson"),
    ("Peter Parker is a photographer who also has a day job as what in some versions?", "High school student or scientist"),
    # Q903: Mossad associated with Israel
    ("What does Mossad mean in Hebrew?", "The Institute (short for Institute for Intelligence and Special Operations)"),
    ("What is the US equivalent of Israel's Mossad?", "CIA (Central Intelligence Agency)"),
    # Q904: East of Argentina = Atlantic Ocean
    ("What ocean is to the west of Argentina?", "Pacific Ocean"),
    ("What is the southernmost tip of South America called?", "Cape Horn"),
    # Q905: First autopsy in 44 BC = Julius Caesar
    ("The first recorded autopsy of Julius Caesar found how many stab wounds?", "23 stab wounds"),
    ("What was Julius Caesar's role in the Roman government?", "Dictator perpetuo (dictator in perpetuity)"),
    # Q906: JFK first sitting president to see American orbiting Earth
    ("Which American was the first to orbit Earth?", "John Glenn (1962)"),
    ("How many orbits did John Glenn make in his historic flight?", "3 orbits"),
    # Q907: Landlocked South American country = Bolivia or Paraguay
    ("Bolivia has two capitals — name them.", "Sucre (constitutional) and La Paz (administrative/government seat)"),
    ("Paraguay is divided by which major river?", "Paraguay River"),
    # Q908: Triceratops horns = 3
    ("What does the prefix 'tri' mean in Triceratops?", "Three (referring to its three horns)"),
    ("What was the name of the large bony structure behind Triceratops' head?", "Frill (or neck frill)"),
    # Q909: First prime after 157 = 163
    ("Is 161 a prime number?", "No (it equals 7 × 23)"),
    ("What is the prime number immediately before 157?", "151"),
    # Q910: Eliza Doolittle in My Fair Lady / Pygmalion
    ("Who wrote the play Pygmalion that inspired My Fair Lady?", "George Bernard Shaw"),
    ("In the musical My Fair Lady, Professor Higgins teaches Eliza to speak properly — what is his field?", "Phonetics"),
    # Q911: Quebec primary language = French
    ("What percentage of Quebec's population speaks French as their first language?", "About 80%"),
    ("What are the two official languages of Canada?", "English and French"),
    # Q912: Capital of El Salvador = San Salvador
    ("El Salvador is the smallest country in which continent?", "Central America"),
    ("What is the currency of El Salvador?", "US dollar (adopted in 2001; also Bitcoin as of 2021)"),
    # Q913: Southernmost city = in Argentina (Ushuaia)
    ("What is the name of the southernmost city in the world?", "Ushuaia, Argentina"),
    ("Ushuaia sits at the southern tip of which island?", "Isla Grande de Tierra del Fuego"),
    # Q914: Newton measures force
    ("A Newton of force is defined as the force needed to accelerate 1 kilogram at what rate?", "1 meter per second squared"),
    ("Isaac Newton described which three fundamental laws of motion?", "Inertia, F=ma, and equal-opposite reaction"),
    # Q915: Rubik's Cube = 6 colors
    ("How many squares are on each face of a standard 3x3 Rubik's Cube?", "9"),
    ("How many possible permutations does a standard 3x3 Rubik's Cube have?", "About 43 quintillion (43,252,003,274,489,856,000)"),
    # Q916: Self-rising flour = flour + salt + baking powder
    ("How much baking powder is typically in one cup of self-rising flour?", "1.5 teaspoons"),
    ("What is another leavening agent sometimes used in baking besides baking powder?", "Baking soda (sodium bicarbonate)"),
    # Q917: Newman Noggs first appeared in Nicholas Nickleby
    ("What is Newman Noggs' role in Nicholas Nickleby?", "He is Ralph Nickleby's clerk who secretly helps Nicholas"),
    ("Nicholas Nickleby was serialized in what form before being published as a book?", "Monthly installments (like most Dickens novels)"),
    # Q918: 97th Miss America held in Las Vegas
    ("In what year was Miss America first televised?", "1954"),
    ("The Miss America pageant was originally held in which city?", "Atlantic City, New Jersey"),
    # Q919: Mexico Independence Day = September 16
    ("Who is credited as the father of Mexican Independence?", "Miguel Hidalgo y Costilla"),
    ("From which country did Mexico gain independence in 1821?", "Spain"),
    # Q920: Pink Floyd associated with inflatable flying pig
    ("Pink Floyd used the flying pig at the premiere of which album?", "Animals (1977)"),
    ("What is the name of Pink Floyd's most famous concept album released in 1979?", "The Wall"),
    # Q921: Miracle on 34th Street = Macy's
    ("In Miracle on 34th Street, who does Kris Kringle claim to be?", "Santa Claus"),
    ("The real Macy's Thanksgiving Day Parade features what type of large decorations?", "Giant helium balloons (shaped like characters)"),
    # Q922: Rainbow Warriors = Hawaii
    ("The University of Hawaii Rainbow Warriors play in which major athletic conference?", "Mountain West Conference"),
    ("What is the state flower of Hawaii?", "Yellow hibiscus (Pua mao hau hele)"),
    # Q923: Snowflake arms = 6
    ("What is the scientific study of snowflakes and ice crystals called?", "Crystallography / glaciology"),
    ("Why do all snowflakes have 6-fold symmetry?", "Due to the molecular structure of water ice (hexagonal crystal lattice)"),
    # Q924: Red Bull from Thailand = Krating Daeng
    ("In what year did Red Bull launch in Austria?", "1987"),
    ("What does 'Krating Daeng' mean in Thai?", "Red gaur (red bull)"),
    # Q925: Leo (born August 15)
    ("What are the dates for the astrological sign Leo?", "July 23 – August 22"),
    ("What is the ruling planet of Leo?", "The Sun"),
    # Q926: Coxswain in rowing
    ("What is the role of a coxswain in crew rowing?", "Steer the boat and coordinate the rowers (faces forward)"),
    ("How many rowers are in an 'eight' rowing event?", "8 rowers plus a coxswain (9 total)"),
    # Q927: Chuck Yeager broke sound barrier in 1940s (1947)
    ("What was the name of Chuck Yeager's aircraft that broke the sound barrier?", "Bell X-1 (also called Glamorous Glennis)"),
    ("Chuck Yeager served in which branch of the US military?", "US Air Force"),
    # Q928: Cube root of 1000 = 10
    ("What is the cube root of 27?", "3"),
    ("What is 10 cubed?", "1,000"),
    # Q929: Porcupine = herbivore
    ("What do porcupines primarily eat?", "Bark, leaves, stems, roots, and berries"),
    ("Are porcupine quills sharp enough to penetrate skin?", "Yes, they are barbed and can embed deeply"),
    # Q930: Willie Loman = Death of a Salesman
    ("Who wrote Death of a Salesman?", "Arthur Miller"),
    ("What year did Death of a Salesman win the Pulitzer Prize?", "1949"),
    # Q931: Florida's theme song = Old Folks at Home (Swanee River)
    ("Who composed 'Old Folks at Home' (Swanee River)?", "Stephen Foster"),
    ("In what year was 'Old Folks at Home' composed?", "1851"),
    # Q932: The View = 5 permanent co-hosts (current)
    ("On what network does The View air?", "ABC"),
    ("The View was created by which television personality?", "Barbara Walters"),
    # Q933: Steve Jobs received a liver transplant
    ("Steve Jobs died in what year?", "2011"),
    ("Steve Jobs co-founded Apple with which two other people?", "Steve Wozniak and Ronald Wayne"),
    # Q934: Highest point on a horse = withers
    ("What is the withers on a horse?", "The highest point of a horse's back, at the base of the neck and between the shoulder blades"),
    ("Horse height is traditionally measured in what units?", "Hands (1 hand = 4 inches)"),
    # Q935: UT head football coach shares name with entertainer = Sarkisian
    ("Steve Sarkisian became UT's head football coach in what year?", "2021"),
    ("What NFL team did Steve Sarkisian work for as an offensive coordinator before UT?", "Alabama Crimson Tide (college) then Atlanta Falcons"),
    # Q936: Rhombus = 4 sides
    ("What is the special name for a rhombus with right angles?", "Square"),
    ("All four sides of a rhombus are equal — true or false?", "True"),
    # Q937: Three major parts of an atom alphabetically = Electron, Neutron, Proton
    ("Which part of the atom carries a negative charge?", "Electron"),
    ("Which part of the atom determines what element it is?", "Proton (atomic number)"),
    # Q938: Super Bowl winner receives Vince Lombardi Trophy
    ("Vince Lombardi coached which NFL team to the first two Super Bowl victories?", "Green Bay Packers"),
    ("How much does the Vince Lombardi Trophy weigh?", "About 7 pounds (3.2 kg)"),
    # Q939: Collarbone = clavicle
    ("The clavicle connects the sternum to which other bone?", "Scapula (shoulder blade)"),
    ("The clavicle is one of the most commonly broken bones — why?", "It bears the brunt of fall impacts when we land on outstretched hands"),
    # Q940: Minimum age for R-rated movie without parent = 17
    ("What does the MPAA rating system stand for?", "Motion Picture Association (formerly Motion Picture Association of America)"),
    ("What rating is given to films appropriate for all audiences?", "G (General Audiences)"),
    # Q941: Summer officially begins in USA in June
    ("What is the astronomical event that marks the official start of summer?", "Summer solstice"),
    ("The summer solstice is the day with the most daylight hours — approximately what date?", "Around June 20-21"),
    # Q942: NHL Mammoth = Salt Lake City
    ("In what year did the NHL Utah Hockey Club (Mammoth) begin play?", "2024-25 season (first year in Utah)"),
    ("The Utah Mammoth are an expansion of which former NHL franchise?", "Arizona Coyotes"),
    # Q943: Ostrich has only 2 toes
    ("Why do ostriches have only 2 toes?", "Evolved for speed — fewer toes means faster running"),
    ("What is the fastest running speed of an ostrich?", "Up to 45 mph (72 km/h)"),
    # Q944: West Side Story gangs = Jets and Sharks
    ("West Side Story is based loosely on which Shakespeare play?", "Romeo and Juliet"),
    ("The 2021 remake of West Side Story was directed by whom?", "Steven Spielberg"),
    # Q945: Most commonly used English consonants = R, S, T
    ("What are the most commonly used letters in English overall (including vowels)?", "E, T, A, O, I, N (in approximate order)"),
    ("Why are R, S, and T printed on a Scrabble tile worth only 1 point?", "They are among the most common letters, making them less valuable"),
    # Q946: Only NY borough attached to mainland = the Bronx
    ("The Bronx is named after which early settler?", "Jonas Bronck (a Swedish-born settler)"),
    ("What two islands make up the main part of New York City's land?", "Manhattan Island and Staten Island (though Queens and Brooklyn are on Long Island)"),
    # Q947: 2026 Chinese Zodiac = Horse (most of the year)
    ("The Year of the Horse is associated with which traits in Chinese astrology?", "Energetic, animated, adventurous, and active"),
    ("How many animals are in the Chinese zodiac?", "12"),
    # Q948: First sign of the Zodiac = Aries
    ("Aries covers which dates in the Western calendar?", "March 21 – April 19"),
    ("What is the symbol/animal for the zodiac sign Aries?", "Ram"),
    # Q949: Snoop Dogg in 'Gin and Juice' recommends orange juice
    ("'Gin and Juice' was released on which Snoop Dogg album?", "Doggystyle (1993)"),
    ("Snoop Dogg's real name is what?", "Calvin Cordozar Broadus Jr."),
    # Q950: La Tomatina = Spain (August)
    ("In which Spanish town is La Tomatina held?", "Buñol, Valencia"),
    ("Approximately how many pounds of tomatoes are thrown at La Tomatina?", "About 150,000 kg (330,000 lbs)"),
    # Q951: Italy's two largest islands = Sicily and Sardinia
    ("Sicily and Sardinia are both islands belonging to which country?", "Italy"),
    ("What is the capital of Sardinia?", "Cagliari"),
    # Q952: Sugar Bear = Golden Crisp cereal mascot
    ("Golden Crisp cereal is made by which company?", "Post Consumer Brands"),
    ("Sugar Bear's slogan for Golden Crisp is what?", "Can't get enough of that Sugar Crisp"),
    # Q953: Largest whale = Blue whale
    ("How long can a blue whale grow?", "Up to about 100 feet (30 meters)"),
    ("Blue whales communicate through what type of sound?", "Low-frequency moaning sounds (infrasound)"),
    # Q954: Egg McMuffin meat = Canadian bacon (ham)
    ("The Egg McMuffin was introduced by McDonald's in what year?", "1972"),
    ("What type of cheese is on an Egg McMuffin?", "American cheese"),
    # Q955: Rudolf Hess died in Spandau Prison in Germany
    ("Rudolf Hess was a top official in Nazi Germany serving in what role?", "Deputy Führer under Adolf Hitler"),
    ("Rudolf Hess famously flew solo to which country in 1941 on a peace mission?", "Scotland (United Kingdom)"),
    # Q956: Scrabble blank tiles = 2 (duplicate question of Q533)
    ("What can a blank Scrabble tile represent?", "Any letter the player chooses"),
    ("Can a blank Scrabble tile be exchanged for its designated letter later in a Scrabble game?", "No, it cannot be swapped once played"),
    # Q957: Plane that dropped A-bomb on Nagasaki = Bockscar
    ("The plane that dropped the bomb on Hiroshima was named what?", "Enola Gay"),
    ("The atomic bomb dropped on Nagasaki was called what?", "Fat Man"),
    # Q958: Solid white flag in NASCAR = one lap remaining
    ("What does a checkered flag mean in NASCAR?", "The race is over — finish line"),
    ("What does a red flag mean in NASCAR?", "Race is stopped (usually for safety)"),
    # Q959: Largest NYC borough by land area = Queens
    ("In which borough is the New York Mets stadium located?", "Queens (Citi Field)"),
    ("What famous international airport is located in Queens, New York?", "John F. Kennedy International Airport (JFK)"),
    # Q960: Amazon founded as 'Cadabra' in 1994
    ("Why did Jeff Bezos change the name from Cadabra to Amazon?", "Cadabra sounded like 'cadaver'; Amazon suggested scale and breadth"),
    ("Amazon's current logo has an arrow that looks like a smile — what does it also represent?", "An arrow from A to Z (meaning Amazon sells everything)"),
    # Q961: Bone formed by ossification
    ("What is the process called when cartilage is converted to bone?", "Ossification (specifically endochondral ossification)"),
    ("What mineral makes bones hard?", "Calcium (and phosphorus)"),
    # Q962: Farfalle = bowtie shape
    ("What does 'farfalle' mean in Italian?", "Butterflies (the bowtie shape resembles butterfly wings)"),
    ("Name another pasta shape named after a physical object or animal.", "(Accept: rigatoni = ridged, fusilli = little spindles, conchiglie = shells, etc.)"),
    # Q963: Brian May co-founded Queen
    ("Brian May plays which instrument in Queen?", "Guitar"),
    ("Brian May has a PhD in what scientific field?", "Astrophysics"),
    # Q964: Magnesium Sulfate = Epsom Salt
    ("What are Epsom salts used for?", "Soaking sore muscles, foot baths, garden fertilizer"),
    ("Epsom salts are named after which English town?", "Epsom, Surrey, England"),
    # Q965: Way of feet and fists = Tae Kwon Do
    ("What does Tae Kwon Do literally mean in Korean?", "The way of foot and fist"),
    ("Tae Kwon Do became an Olympic sport in what year?", "2000 (Sydney Olympics)"),
    # Q966: Alcatraz named for pelican (Spanish)
    ("What Spanish word meaning pelican gave Alcatraz its name?", "Alcatraces (pelicans)"),
    ("Alcatraz Island sits in which California bay?", "San Francisco Bay"),
    # Q967: Iron Pyrite = Fool's Gold
    ("Why is iron pyrite called Fool's Gold?", "It resembles gold in color but is worthless — it fooled many prospectors"),
    ("What chemical formula is iron pyrite?", "FeS₂ (iron disulfide)"),
    # Q968: New Delhi replaced Calcutta as India's capital in 1911
    ("New Delhi was built as a planned capital — construction completed in what year?", "1931"),
    ("Calcutta (now Kolkata) is located on which Indian river?", "Hooghly River (a distributary of the Ganges)"),
    # Q969: China's flag = 5 stars
    ("What do the stars on China's flag represent?", "One large star (CCP) and four smaller stars (four social classes united)"),
    ("What color is the background of China's national flag?", "Red"),
    # Q970: Highest US civilian honor = Presidential Medal of Freedom
    ("Who created the Presidential Medal of Freedom?", "John F. Kennedy (1963)"),
    ("What is the highest military honor in the United States?", "Medal of Honor"),
    # Q971: Great Barrier Reef off coast of Australia
    ("The Great Barrier Reef is the world's largest what?", "Coral reef system"),
    ("The Great Barrier Reef is located off the coast of which Australian state?", "Queensland"),
    # Q972: Romeo and Juliet set in Verona
    ("In what Italian region is Verona located?", "Veneto"),
    ("What is the name of Juliet's family in Romeo and Juliet?", "Capulet"),
    # Q973: Alphabetically first among NV, IA, NH, CO capitals = Carson City
    ("What is the capital of Iowa?", "Des Moines"),
    ("What is the capital of Colorado?", "Denver"),
    # Q974: Jennifer Lopez has 37+ scents = Limitless, Promise
    ("Jennifer Lopez launched her first perfume with what name?", "Glow by J.Lo (2002)"),
    ("Jennifer Lopez's perfume line is one of the bestselling celebrity fragrance lines — what industry record did she set?", "One of the highest-grossing celebrity perfume lines ever"),
    # Q975: Pilgrims landed in 1600s (1620)
    ("In what month and year did the Pilgrims land at Plymouth?", "November 1620"),
    ("On what ship did the Pilgrims travel to America?", "Mayflower"),
    # Q976: Wasabi = green horseradish paste
    ("True wasabi comes from which plant?", "Wasabia japonica (Japanese horseradish)"),
    ("Most wasabi served outside Japan is made from what?", "European horseradish with green food coloring"),
    # Q977: Warthog has 4 tusks
    ("Where do warthogs live?", "African savannahs and grasslands"),
    ("What do warthogs use their tusks for?", "Defense, digging, and fighting other warthogs"),
    # Q978: New Year's Day birthday = Capricorn
    ("What are the dates of the Capricorn astrological sign?", "December 22 – January 19"),
    ("What animal represents Capricorn?", "Sea goat"),
    # Q979: Russia and Turkey share Black Sea coastline
    ("How many countries border the Black Sea?", "6 (Bulgaria, Romania, Ukraine, Russia, Georgia, Turkey)"),
    ("What strait connects the Black Sea to the Mediterranean?", "Bosphorus Strait (through the Sea of Marmara and Dardanelles)"),
    # Q980: Indoor volleyball active players = 6
    ("How many players total can be on a volleyball roster in indoor volleyball?", "12-14 players"),
    ("In volleyball, what is the specialized defensive player who can substitute freely?", "Libero"),
    # Q981: Herbie Hancock = piano
    ("Herbie Hancock was part of which legendary jazz musician's ensemble in the 1960s?", "Miles Davis"),
    ("What 1983 Herbie Hancock hit became one of the first hip-hop-influenced jazz records?", "Rockit"),
    # Q982: UT Men's Basketball Coach last name = Terry (Rodney Terry)
    ("Rodney Terry became UT's head coach permanently after the team's success in what year?", "2023 (after Elite Eight run)"),
    ("The University of Texas Longhorns play in which NCAA conference?", "SEC (Southeastern Conference)"),
    # Q983: Shift-5 = %
    ("What symbol is produced by pressing Shift-4 on a standard keyboard?", "$ (dollar sign)"),
    ("What symbol is produced by pressing Shift-8?", "* (asterisk)"),
    # Q984: Dickens wrote all: Christmas Carol, Great Expectations, Edwin Drood, others
    ("The Mystery of Edwin Drood was left unfinished by Dickens at the time of his death — true or false?", "True"),
    ("Great Expectations features which memorable jilted woman character who stopped all the clocks?", "Miss Havisham"),
    # Q985: i in HDMI = Interface
    ("What does HDMI stand for?", "High-Definition Multimedia Interface"),
    ("HDMI cables transmit which two types of data?", "Video and audio"),
    # Q986: Reflex angle > 180 degrees
    ("What is an angle of exactly 180 degrees called?", "Straight angle"),
    ("An angle less than 90 degrees is called what?", "Acute angle"),
    # Q987: Battle of Bull Run in Civil War
    ("The Battle of Bull Run (also called First Manassas) took place in which state?", "Virginia"),
    ("Who won the First Battle of Bull Run?", "Confederate forces"),
    # Q988: Most northern among Miami, Orlando, Tampa, Palm Beach = Orlando
    ("What theme park is located in Orlando, Florida?", "Walt Disney World (and Universal Studios, SeaWorld)"),
    ("Orlando is in which Florida county?", "Orange County"),
    # Q989: Hockey hat trick = 3 goals minimum
    ("What is the term for scoring 4 goals in one hockey game?", "Gordie Howe hat trick (also just '4 goals')"),
    ("Why is three goals called a hat trick in hockey?", "From cricket tradition where a bowler who took 3 wickets received a hat"),
    # Q990: Nathan Hale quote = 'I only regret that I have but one life to lose'
    ("Nathan Hale was hanged by the British as a spy during which war?", "American Revolutionary War"),
    ("How old was Nathan Hale when he was executed?", "21 years old"),
    # Q991: Greenpeace headquarters = Amsterdam
    ("Greenpeace was founded in which country?", "Canada (Vancouver, British Columbia)"),
    ("What is Greenpeace's primary focus?", "Environmental activism and conservation"),
    # Q992: Harvard = first US college (1636)
    ("Harvard University is located in which Massachusetts city?", "Cambridge"),
    ("What professional sports team in Boston shares its deep crimson color with Harvard?", "Boston Red Sox (though they're red, not crimson — Harvard's color is Crimson)"),
    # Q993: West Virginia seceded from Virginia in 1863
    ("West Virginia became the how-manyth US state?", "35th state"),
    ("West Virginia is the only state formed by seceding from another state during the Civil War — true or false?", "True"),
    # Q994: Cinderella had 2 evil stepsisters
    ("What are the names of Cinderella's stepsisters in the Disney version?", "Anastasia and Drizella"),
    ("What did Cinderella leave behind at the ball?", "Her glass slipper"),
    # Q995: Superman 2025 actor = David Corenswet
    ("In what year was the 2025 Superman film released?", "2025"),
    ("The 2025 Superman film was written and directed by whom?", "James Gunn"),
    # Q996: MENSA = table in Latin
    ("MENSA is an organization for people with what characteristic?", "High IQ (top 2% of the population)"),
    ("What IQ score is typically required to join MENSA?", "130 or above"),
    # Q997: 88-key piano black keys = 36
    ("How many white keys are on an 88-key piano?", "52"),
    ("How many octaves are on a standard 88-key piano?", "7 octaves plus a few extra notes"),
    # Q998: Green light on starboard (right) side of ship
    ("What color light is on the port (left) side of a ship?", "Red"),
    ("What does the green starboard light and red port light help ships determine?", "The direction of travel of other vessels (avoid collision)"),
    # Q999: Taylor Swift 2025 tour = Eras Tour
    ("The Eras Tour by Taylor Swift became the highest-grossing concert tour of all time — true or false?", "True"),
    ("The Eras Tour featured how many acts or 'eras' from Taylor Swift's discography?", "10 eras (approximately)"),
    # Q1000: Vietnam does NOT border North Korea
    ("What four countries actually border North Korea?", "China, South Korea, Russia, and the Yellow Sea/Korea Bay (ocean)"),
    ("North Korea and South Korea are separated by what zone?", "Demilitarized Zone (DMZ)"),
    # Q1001: LXXX = 80
    ("In Roman numerals, what does XC mean?", "90"),
    ("What Roman numeral represents 40?", "XL"),
    # Q1002: Unlucky to say 'Macbeth' in theater
    ("What is the superstition around saying 'Macbeth' in a theater?", "It is said to bring bad luck to the production"),
    ("What do theater people call Macbeth instead of its name?", "The Scottish Play"),
    # Q1003: Battle of Waterloo = Belgium
    ("In what year was the Battle of Waterloo fought?", "1815"),
    ("Who defeated Napoleon at the Battle of Waterloo?", "Duke of Wellington and Prussian forces (Blücher)"),
    # Q1004: Mea Culpa = I am to blame
    ("Mea Culpa is Latin — what does 'mea' mean?", "My/mine"),
    ("In what context is 'Mea Culpa' often used today?", "Admission of fault or personal apology"),
    # Q1005: University of Kansas = Lawrence, Kansas
    ("The University of Kansas Jayhawks compete in which athletic conference?", "Big 12 Conference"),
    ("What is a jayhawk?", "A mythical bird combining a blue jay and a sparrow hawk"),
    # Q1006: Will Muschamp left South Carolina to return to UT
    ("Will Muschamp served as UT's defensive coordinator before becoming a head coach at which school first?", "University of Florida"),
    ("In what year did Will Muschamp return to Texas as defensive coordinator?", "2023"),
    # Q1007: Rub a Dub Dub — 3 men jumped out of a tub
    ("Who are the three men in the tub in the rhyme 'Rub a Dub Dub'?", "A butcher, a baker, and a candlestick maker"),
    ("The nursery rhyme 'Rub a Dub Dub' originally came from which country?", "England"),
    # Q1008: Scrivener = writer
    ("What famous Melville short story features a character named Bartleby the Scrivener?", "Bartleby, the Scrivener by Herman Melville"),
    ("Historically, what tools did scriveners use to copy documents?", "Quill pens and ink"),
    # Q1009: Proper name for note neither sharp nor flat = natural
    ("In music notation, what symbol indicates a natural note?", "A natural sign (♮)"),
    ("What is a note that is raised a half step called?", "Sharp (♯)"),
    # Q1010: Division answer = quotient
    ("In mathematics, what is the term for the number being divided?", "Dividend"),
    ("What is the term for the number you divide by in a division problem?", "Divisor"),
    # Q1011: Andrew Lloyd Webber most successful musical = Phantom of the Opera
    ("Andrew Lloyd Webber also composed which other famous musical set in a Buenos Aires?", "Evita"),
    ("Cats is another Lloyd Webber musical — it's based on poems by which author?", "T.S. Eliot"),
    # Q1012: Mayo Clinic headquarters = Rochester, Minnesota
    ("In what year was the Mayo Clinic founded?", "1889"),
    ("The Mayo Clinic is named after which father and son medical duo?", "Dr. William Worrall Mayo, Dr. William James Mayo, and Dr. Charles Horace Mayo"),
    # Q1013: Last studio album by Beatles = Let It Be (May 1970)
    ("Let It Be was the last album released by the Beatles but was actually recorded before which other album?", "Abbey Road"),
    ("Who produced the Let It Be album?", "Phil Spector (controversially) and originally Glyn Johns"),
    # Q1014: The Great Gatsby character's first name = Jay
    ("Who wrote The Great Gatsby?", "F. Scott Fitzgerald"),
    ("In what year was The Great Gatsby published?", "1925"),
    # Q1015: City of Ephesus in modern Turkey
    ("The ruins of Ephesus contain one of the Seven Wonders of the Ancient World — which one?", "Temple of Artemis"),
    ("Paul the Apostle wrote an Epistle (letter) to the Christians of which ancient city?", "Ephesus (The Epistle to the Ephesians)"),
    # Q1016: Yellow Brick Road leads to Emerald City
    ("Who lives in the Emerald City?", "The Wizard of Oz"),
    ("What is Dorothy's last name in The Wizard of Oz?", "Gale"),
    # Q1017: Skink = lizard
    ("How many species of skinks are there approximately?", "Over 1,500 species"),
    ("Skinks are notable for what unusual trait compared to many other lizards?", "They have smooth, overlapping scales (and many species can drop their tail as a defense)"),
    # Q1018: Hardy Boys = Frank and Joe
    ("Who created the Hardy Boys mystery series?", "Franklin W. Dixon (house pseudonym for Stratemeyer Syndicate)"),
    ("What is the name of the Hardy Boys' father, who is also a famous detective?", "Fenton Hardy"),
    # Q1019: Singer with #1 hit 'Opalite' = Taylor Swift
    ("What album is 'Opalite' from?", "The Tortured Poets Department (2024)"),
    ("Taylor Swift's genre spans which two major musical styles?", "Country and pop"),
    # Q1020: Dolly Parton's #1 hit = 9 to 5
    ("In what year was Dolly Parton's '9 to 5' released?", "1980"),
    ("'9 to 5' was written for which film starring Dolly Parton?", "9 to 5 (the film of the same name)"),
    # Q1021: Hoover Dam separates Arizona and Nevada
    ("What river does the Hoover Dam block to form Lake Mead?", "Colorado River"),
    ("When was the Hoover Dam completed?", "1936"),
    # Q1022: Monopoly patterned after Atlantic City, NJ
    ("What are the most expensive properties in Monopoly?", "Boardwalk and Park Place"),
    ("In what year was Monopoly first sold commercially?", "1935"),
    # Q1023: Snake smells through its tongue
    ("What organ do snakes use to process the scent particles collected by their tongues?", "Jacobson's organ (vomeronasal organ)"),
    ("Are all snakes venomous?", "No, only about 600 of 3,700+ species are venomous"),
    # Q1024: Davy Crockett born in Greene County, Tennessee
    ("What famous battle is Davy Crockett known for dying at?", "Battle of the Alamo (1836)"),
    ("Davy Crockett is known for wearing a hat made from what animal?", "Raccoon"),
    # Q1025: 4th Pac-Man ghost = Clyde
    ("What color is the Pac-Man ghost named Clyde?", "Orange"),
    ("What is the name of the power pellet in Pac-Man that lets you eat ghosts?", "Power pellet (or energizer)"),
    # Q1026: D in WD-40 = Displacing (Water-Displacing)
    ("What does the '40' in WD-40 stand for?", "The 40th attempt to perfect the formula"),
    ("WD-40 was originally developed for which aerospace company?", "Convair (for the Atlas rocket)"),
    # Q1027: Brisket = from the chest of a cow
    ("Texas BBQ is famous for which style of cooking brisket?", "Low and slow smoking (offset smoker)"),
    ("What wood is most traditionally used to smoke brisket in Texas?", "Post oak"),
    # Q1028: Clarence Thomas appointed by George H.W. Bush in 1991
    ("Clarence Thomas has served as the longest-sitting Justice on which court?", "US Supreme Court"),
    ("Clarence Thomas's 1991 confirmation hearings were controversial due to testimony from whom?", "Anita Hill"),
    # Q1029: Belmont Stakes = 12 furlongs (longest Triple Crown race)
    ("A furlong is equal to how many yards?", "220 yards (1/8 of a mile)"),
    ("The Kentucky Derby, by comparison, is how many furlongs?", "10 furlongs (1.25 miles)"),
    # Q1030: Glinda in 2024 Wicked = Ariana Grande
    ("Who played the role of Elphaba (the Wicked Witch) in the 2024 Wicked film?", "Cynthia Erivo"),
    ("What 2024 film featured Ariana Grande as Glinda the Good Witch?", "Wicked"),
    # Q1031: Herbert Hoover was president when Great Depression started
    ("What event in October 1929 is often cited as the start of the Great Depression?", "Black Tuesday (stock market crash on October 29, 1929)"),
    ("Herbert Hoover was succeeded as president by whom?", "Franklin D. Roosevelt"),
    # Q1032: Quasimodo = bell ringer at Notre-Dame de Paris
    ("Who wrote The Hunchback of Notre-Dame?", "Victor Hugo"),
    ("What is the name of the gypsy woman Quasimodo loves in The Hunchback?", "Esmeralda"),
    # Q1033: Wicked Witch of the East was killed by Dorothy's falling house
    ("In The Wizard of Oz, who is the main villain?", "Wicked Witch of the West"),
    ("What did the Wicked Witch of the East leave behind after she was killed?", "Her ruby slippers"),
    # Q1034: Puppy paws (pair of 5s) = 10 in craps
    ("In craps, what is a roll of two 1s (snake eyes) called?", "Snake eyes"),
    ("What is rolling two 6s in craps called?", "Boxcars or midnight"),
    # Q1035: Mr. Clean first name since 1962 = Veritably
    ("Mr. Clean is a cleaning product made by which company?", "Procter & Gamble"),
    ("In what year did Mr. Clean first appear in commercials?", "1958"),
    # Q1036: AC/DC founding brothers = Young (Angus and Malcolm Young)
    ("Angus Young is known for wearing what costume on stage?", "A school uniform (blazer and shorts)"),
    ("AC/DC was founded in which country?", "Australia"),
    # Q1037: Teddy and FDR both governed New York
    ("Franklin D. Roosevelt was elected governor of New York in what year?", "1928"),
    ("Theodore Roosevelt served as NY governor from which years?", "1899-1900"),
    # Q1038: Copper from Cyprus (Latin: Cuprum)
    ("What is copper's chemical symbol?", "Cu"),
    ("Copper is the third most consumed industrial metal after what two metals?", "Iron and aluminum"),
    # Q1039: Alabama bordered to north by Tennessee
    ("What state is directly south of Alabama?", "Florida (and the Gulf of Mexico)"),
    ("Birmingham, Alabama's largest city, was once known as the what of the South?", "Pittsburgh of the South (for steel production)"),
    # Q1040: CBS first color TV program in 1951
    ("What was the first color TV program in the US broadcast?", "CBS's first scheduled color broadcast"),
    ("What year did color television become widely available to consumers?", "Late 1950s to 1960s"),
    # Q1041: Oscar is both an award name and NATO phonetic alphabet letter
    ("What letter does 'Oscar' represent in the NATO phonetic alphabet?", "O"),
    ("The Oscar statuette depicts a knight holding a crusader's sword standing on a what?", "A reel of film"),
    # Q1042: Billy Bob Thornton's band = The Boxmasters
    ("Billy Bob Thornton is also famous for his work as what in Hollywood?", "Actor, writer, and director"),
    ("What 1996 film did Billy Bob Thornton write, direct, and star in to great acclaim?", "Sling Blade"),
    # Q1043: Standard harmonica has 10 holes
    ("What type of harmonica is used most in blues music?", "Diatonic harmonica (10-hole harmonica)"),
    ("How many notes can a typical 10-hole harmonica produce?", "20 notes (blow and draw for each hole)"),
    # Q1044: Delaware first state to ratify US Constitution
    ("What is Delaware's nickname related to being first?", "The First State"),
    ("In what year did Delaware ratify the US Constitution?", "1787"),
    # Q1045: Hippocrates = Greek (father of modern medicine)
    ("Hippocrates lived on which Greek island?", "Cos (Kos)"),
    ("What oath, named after Hippocrates, do doctors take?", "Hippocratic Oath"),
    # Q1046: Big Sky = Montana's license plate
    ("What is Montana's state capital?", "Helena"),
    ("Montana is the 4th largest US state — what is the largest city in Montana?", "Billings"),
    # Q1047: US president who fathered 15 children = John Tyler
    ("John Tyler was the first president to do what unusual thing?", "Have his vice presidency vacated / be expelled from his own party (Whig)"),
    ("John Tyler's nickname was 'His Accidency' because he became president how?", "By succeeding William Henry Harrison who died after 31 days in office"),
    # Q1048: Valencia oranges from Spain
    ("Valencia, Spain is in which autonomous community?", "Community of Valencia"),
    ("Valencia oranges are named for the city of Valencia — true or false?", "True (the orange was named after the city in Spain)"),
    # Q1049: Hogwarts train leaves from Platform 9 3/4
    ("Which London train station has Platform 9 3/4?", "King's Cross Station"),
    ("What is the name of the school train that goes to Hogwarts?", "Hogwarts Express"),
    # Q1050: Only other egg-laying mammal besides echidna = platypus
    ("What order do egg-laying mammals belong to?", "Monotremata (monotremes)"),
    ("Besides laying eggs, what other surprising feature does a platypus have?", "A bill like a duck, venomous spur (males), and detects prey with electroreception"),
    # Q1051: Benny Blanco's wife = Selena Gomez
    ("Selena Gomez is also known for her acting on which Disney TV show?", "Wizards of Waverly Place"),
    ("Benny Blanco has produced hits for which famous pop artist?", "Katy Perry, Ed Sheeran, Maroon 5 (accept any)"),
    # Q1052: Paella from Spain
    ("What is the main grain in traditional paella?", "Rice"),
    ("Paella originated in which Spanish region?", "Valencia"),
    # Q1053: LinkedIn parent company = Microsoft
    ("Microsoft acquired LinkedIn in what year?", "2016"),
    ("Approximately how much did Microsoft pay for LinkedIn?", "About $26.2 billion"),
    # Q1054: Lambeau Field filled with Cheeseheads = Green Bay Packers
    ("What city is Lambeau Field located in?", "Green Bay, Wisconsin"),
    ("The Green Bay Packers are unique in the NFL for being owned how?", "Community-owned (publicly owned nonprofit)"),
    # Q1055: Pinocchio cat = Figaro (also opera character)
    ("What famous opera features the character Figaro?", "The Barber of Seville and The Marriage of Figaro"),
    ("In Pinocchio, what is the name of the wooden puppet's cricket companion?", "Jiminy Cricket"),
    # Q1056: ISO rating = photo film speed
    ("In modern digital photography, what does ISO control?", "Sensor sensitivity to light"),
    ("Higher ISO settings in photography result in what?", "Brighter images but more grain/noise"),
    # Q1057: Suriname in South America
    ("What is the capital of Suriname?", "Paramaribo"),
    ("Suriname is a former colony of which European country?", "Netherlands (Dutch Guiana)"),
    # Q1058: Current UFC CEO = Dana White
    ("Dana White became president of the UFC in what year?", "2001"),
    ("What does UFC stand for?", "Ultimate Fighting Championship"),
    # Q1059: Olympic Individual Medley first stroke = butterfly
    ("What are the four strokes in the Individual Medley in order?", "Butterfly, backstroke, breaststroke, freestyle"),
    ("In what year was the Individual Medley added to the Olympic swimming program?", "1964 (Tokyo Olympics)"),
    # Q1060: Far rear left in orchestra = percussion
    ("What family of instruments sits at the very front of a typical orchestra?", "Strings"),
    ("Where do the woodwinds typically sit in an orchestra?", "In the middle (between strings in front and brass behind)"),
    # Q1061: Montana, Utah, Wyoming, None — borders Oregon = None
    ("Which US states do border Oregon?", "Washington, Idaho, Nevada, and California"),
    ("Oregon's largest city is what?", "Portland"),
    # Q1062: Pommel of saddle = at the front
    ("What is the rear elevated part of a saddle called?", "Cantle"),
    ("The pommel is also the top of what weapon?", "A sword (the knob at the end of the handle)"),
    # Q1063: Phantom of the Opera lived in sewers of Paris
    ("The Phantom of the Opera musical was composed by whom?", "Andrew Lloyd Webber"),
    ("What does the Phantom wear to hide his face?", "A mask (covering the right side of his face)"),
    # Q1064: The Raven's deceased lover = Lenore
    ("Who wrote 'The Raven'?", "Edgar Allan Poe"),
    ("In what year was 'The Raven' published?", "1845"),
    # Q1065: University of Colorado buffalo mascot = Ralphie
    ("The University of Colorado Buffaloes play in which athletic conference?", "Big 12 Conference"),
    ("What is the hometown of the University of Colorado?", "Boulder, Colorado"),
    # Q1066: Earth closest to sun in January
    ("What is the point when Earth is closest to the Sun called?", "Perihelion"),
    ("What is the point when Earth is farthest from the Sun called?", "Aphelion"),
    # Q1067: K-Pop from South Korea
    ("What does K-Pop stand for?", "Korean Pop"),
    ("Name one of the most famous K-Pop groups globally.", "BTS or BLACKPINK (accept any well-known group)"),
    # Q1068: DTMF Hot 100 song = Bad Bunny
    ("What does DTMF stand for in Bad Bunny's song title?", "Deja Tú y Yo que hablemos More (or: Don't Tell Me Farewell)"),
    ("Bad Bunny broke streaming records in which year?", "2020, 2021, and 2022 (consecutively)"),
    # Q1069: Most oysters born male
    ("Oysters can change sex during their lifetime — this is called what?", "Sequential hermaphroditism"),
    ("What is the process called when oysters produce pearls?", "The pearl forms around an irritant that the oyster coats with nacre"),
    # Q1070: Fax = facsimile
    ("Fax machines transmit documents over what type of network?", "Telephone network"),
    ("What does 'facsimile' mean literally?", "Make similar / exact copy"),
    # Q1071: Roly poly has more than 12 legs (14 legs)
    ("What is another common name for the roly poly?", "Pill bug or woodlouse"),
    ("A roly poly is not an insect — what is it?", "A crustacean (isopod)"),
    # Q1072: Cilantro leaf = from coriander plant
    ("In British English, what is cilantro called?", "Coriander (the leaves are called coriander, not cilantro)"),
    ("What flavor do some people perceive in cilantro that others find appealing?", "Soapy (due to a genetic trait related to aldehyde-detecting receptors)"),
    # Q1073: Most recent Heisman Trophy winner = Mendoza
    ("The Heisman Trophy is presented in what city each year?", "New York City"),
    ("Fernando Mendoza played quarterback for which college team?", "California (Cal Bears)"),
    # Q1074: Washington Monument taller than Statue of Liberty and Great Pyramid
    ("What is the height of the Washington Monument?", "555 feet (169 m)"),
    ("The Washington Monument was the world's tallest structure from 1884 until what was built?", "Eiffel Tower (1889)"),
    # Q1075: Shrimp are crustaceans (oyster, clam, starfish are not)
    ("What makes shrimp a crustacean rather than a mollusk?", "Shrimp have exoskeletons and jointed legs; mollusks have shells"),
    ("Name three other crustaceans besides shrimp.", "Crab, lobster, crayfish, barnacle, krill (accept any)"),
    # Q1076: Billboard top song 2025 = 'Die With a Smile' Lady Gaga & Bruno Mars
    ("In what year did Lady Gaga and Bruno Mars release 'Die With a Smile'?", "2024"),
    ("Lady Gaga's real name is what?", "Stefani Joanne Angelina Germanotta"),
    # Q1077: NHL bird teams = 3 (Penguins, Ducks, historically Senators)
    ("The Pittsburgh Penguins are named after a bird native to which hemisphere?", "Southern Hemisphere (penguins are not native to Pittsburgh — the name was chosen by a contest)"),
    ("The Anaheim Ducks were originally named after which Disney movie?", "The Mighty Ducks (1992)"),
    # Q1078: Mason-Dixon line = northern border of Maryland
    ("Who were Mason and Dixon, for whom the line is named?", "Charles Mason and Jeremiah Dixon (surveyors)"),
    ("The Mason-Dixon line was originally surveyed to settle a border dispute between which colonies?", "Pennsylvania and Maryland"),
    # Q1079: Warren Buffett claims to eat at McDonald's every day
    ("Warren Buffett is known for living frugally despite his wealth — true or false?", "True"),
    ("What is Warren Buffett's famous advice about investing?", "Buy and hold quality companies for the long term; be fearful when others are greedy"),
    # Q1080: US states bordering Pacific = 5
    ("Name the five US states that border the Pacific Ocean.", "Alaska, Hawaii, Washington, Oregon, California"),
    ("Which Pacific-bordering state is not part of the contiguous 48 states?", "Alaska and Hawaii"),
    # Q1081: Christopher Walken pitchman for Miller Lite / Heineken
    ("Christopher Walken is known for his role in which 1978 Oscar-winning Vietnam War film?", "The Deer Hunter"),
    ("Christopher Walken played an iconic villain in which James Bond film?", "A View to a Kill"),
    # Q1082: Sonnet = 14 lines
    ("A Shakespearean sonnet consists of how many stanzas?", "3 quatrains and 1 couplet"),
    ("What is the rhyme scheme of the final couplet in a Shakespearean sonnet?", "GG (rhyming couplet)"),
    # Q1083: Peter the Great founded Russia (as a modern state)
    ("Peter the Great built which new Russian capital city on the Baltic Sea?", "Saint Petersburg"),
    ("In what year did Peter the Great begin his rule?", "1682 (officially 1696 as sole ruler)"),
    # Q1084: Ark of the Covenant held the Ten Commandments
    ("In the Bible, the Ark of the Covenant was kept in what sacred location in Solomon's Temple?", "The Holy of Holies"),
    ("According to the book of Exodus, on what material were the Ten Commandments written?", "Stone tablets"),
    # Q1085: Albuquerque in Chihuahuan Desert
    ("What is the largest desert in North America?", "Great Basin Desert"),
    ("The Chihuahuan Desert spans the border of which two countries?", "United States and Mexico"),
    # Q1086: Capital of South Carolina = Columbia
    ("Columbia, South Carolina, was partially burned during which war?", "Civil War (Sherman's March)"),
    ("What major university is located in Columbia, South Carolina?", "University of South Carolina"),
    # Q1087: Nonet = 9 voices or instruments
    ("What is a musical piece for 8 performers called?", "Octet"),
    ("What is a musical piece for 7 performers called?", "Septet"),
    # Q1088: Managua = capital of Nicaragua
    ("Managua is located on the shore of which lake?", "Lake Managua (Lake Xolotlán)"),
    ("Nicaragua is the largest country in what region?", "Central America"),
    # Q1089: James Bond's boss = M
    ("Who plays M in many of the modern James Bond films (the woman)?", "Judi Dench"),
    ("James Bond works for which British intelligence agency?", "MI6 (Secret Intelligence Service)"),
    # Q1090: Daguerreotype = early photo
    ("Who invented the daguerreotype?", "Louis Daguerre"),
    ("In what year was the daguerreotype process publicly announced?", "1839"),
    # Q1091: Epilation = hair removal
    ("What is the difference between epilation and depilation?", "Epilation removes hair from the root; depilation removes only the hair above the skin"),
    ("Laser hair removal is a form of what — epilation or depilation?", "Epilation (it destroys the hair follicle)"),
    # Q1092: College World Series of Baseball = Omaha, Nebraska
    ("In what stadium is the College World Series held?", "Charles Schwab Field Omaha (formerly TD Ameritrade Park)"),
    ("The College World Series features how many teams?", "8 teams"),
    # Q1093: Chimay = Belgian Trappist beer
    ("Chimay beer is brewed by monks at which abbey in Belgium?", "Scourmont Abbey"),
    ("What is the most distinctive feature of Trappist beers' production?", "They must be brewed within the walls of a Trappist monastery by or under the supervision of monks"),
    # Q1094: Basketball Hall of Fame = Massachusetts (Springfield)
    ("The Basketball Hall of Fame is located in Springfield, Massachusetts — why Springfield?", "Basketball was invented there by James Naismith in 1891"),
    ("Who invented basketball?", "James Naismith"),
    # Q1095: Nightwing's mentor = Batman
    ("What is Nightwing's real name?", "Dick Grayson"),
    ("Dick Grayson was previously known by what superhero name before becoming Nightwing?", "Robin (the first Robin)"),
    # Q1096: Washington Crossing the Delaware depicts Battle of Trenton
    ("When did George Washington cross the Delaware River?", "December 25-26, 1776"),
    ("Who painted Washington Crossing the Delaware?", "Emanuel Leutze (1851)"),
    # Q1097: Minimum age for US House = 25
    ("What is the minimum age to serve in the US Senate?", "30 years old"),
    ("What is the minimum age to run for US President?", "35 years old"),
    # Q1098: Julienne = French knife technique for matchstick vegetables
    ("What is the French culinary term for cutting vegetables into very thin slices?", "Chiffonade (for leafy vegetables) or mandoline cuts"),
    ("What is the French term for cutting food into small, uniform cubes?", "Brunoise (small) or dice (larger)"),
    # Q1099: Southernmost capital in contiguous US = Austin, Texas
    ("What is the southernmost state capital in the US (including Hawaii)?", "Honolulu, Hawaii"),
    ("Austin is the capital of Texas — what is the largest city in Texas?", "Houston"),
    # Q1100: Heifer = cow that has not had a calf
    ("What is a female pig before she has a litter called?", "Gilt"),
    ("What is a young female horse (under 4 years) called?", "Filly"),
    # Q1101: Labyrinth built by Daedalus for the Minotaur
    ("Who commissioned Daedalus to build the labyrinth?", "King Minos of Crete"),
    ("Daedalus and his son Icarus escaped from Crete using wings of wax and feathers — what happened to Icarus?", "He flew too close to the sun, which melted the wax, and he fell into the sea"),
    # Q1102: Mills Bomb = hand grenade
    ("The Mills Bomb was used extensively in which two world wars?", "World War I and World War II"),
    ("What safety mechanism prevents a hand grenade from exploding prematurely?", "Safety pin / pull ring (and safety lever/spoon)"),
    # Q1103: Limerick = 5 lines
    ("What is the rhyme scheme of a limerick?", "AABBA"),
    ("In what city of Ireland did limericks originate (or become associated)?", "Limerick, Ireland"),
    # Q1104: Eiswein = wine from frozen grapes
    ("Eiswein is a German term meaning what in English?", "Ice wine"),
    ("What country is the largest producer of ice wine (Eiswein) outside Germany?", "Canada"),
    # Q1105: Spring and neap = types of tides
    ("A spring tide occurs during which lunar phases?", "New moon and full moon (when sun, Earth, and moon are aligned)"),
    ("A neap tide occurs when the moon is in what phase?", "First and third quarter (when sun and moon are at right angles to Earth)"),
    # Q1106: Gulliver's first name = Lemuel
    ("Who wrote Gulliver's Travels?", "Jonathan Swift"),
    ("In Gulliver's Travels, the Lilliputians are how tall compared to Gulliver?", "About 6 inches tall (1/12 of Gulliver's size)"),
    # Q1107: Trichology = study of hair
    ("What type of doctor specializes in hair and scalp disorders?", "Dermatologist (or trichologist — a hair specialist)"),
    ("What is the medical term for hair loss?", "Alopecia"),
    # Q1108: Pluvial = related to rain
    ("What is the study of rainfall and precipitation called?", "Hydrology (or hydrometeorology for precipitation specifically)"),
    ("'Pluvial' comes from the Latin word for what?", "Rain (pluvia)"),
    # Q1109: Tabla = percussion family
    ("The tabla is a pair of drums originating from which country?", "India"),
    ("What musical genre most commonly features the tabla?", "Hindustani classical music (North Indian classical music)"),
    # Q1110: Legal age of consent in Texas = XVII (17)
    ("What numeral represents 17 in Roman numerals?", "XVII"),
    ("How do you write 20 in Roman numerals?", "XX"),
    # Q1111: First number to contain 'A' when spelled out = thousand
    ("What is the first number to contain the letter 'B' when spelled out?", "Billion"),
    ("How do you spell the number 1,000 in words?", "One thousand"),
    # Q1112: Lox = salmon
    ("What is lox typically made from?", "Cured (salt-cured) salmon"),
    ("What is the difference between lox and smoked salmon?", "Lox is brined/cured; smoked salmon is also smoked after curing"),
    # Q1113: Sea anemone = animal
    ("What do sea anemones eat?", "Small fish and shrimp (invertebrates and small creatures)"),
    ("What famous clownfish character lives with a sea anemone in the film Finding Nemo?", "Nemo (Marlin's son)"),
    # Q1114: Brooklyn Bridge crosses the East River
    ("In what year was the Brooklyn Bridge completed?", "1883"),
    ("The Brooklyn Bridge connects Brooklyn to which other NYC borough?", "Manhattan"),
    # Q1115: Soft hand in blackjack contains an ace
    ("Why is an ace called a 'soft' hand in blackjack?", "An ace can count as 1 or 11, giving flexibility without busting"),
    ("In blackjack, what is the best possible hand?", "Blackjack (an ace + 10-point card)"),
    # Q1116: Hockey goal width = 6 feet
    ("What is the height of an NHL hockey goal?", "4 feet"),
    ("What material are the posts and crossbar of an NHL goal made of?", "Steel (painted red)"),
    # Q1117: Dolly Parton #1 hit = 9 to 5 (duplicate of Q1020)
    ("Besides singing, Dolly Parton is known for which other career?", "Songwriting and philanthropy (Imagination Library)"),
    ("Dolly Parton turned down the Presidential Medal of Freedom twice before accepting — true or false?", "True (she declined twice before accepting under Biden)"),
    # Q1118: John Adams related to John Quincy Adams = father and son
    ("John Adams was the 2nd US President — what number was John Quincy Adams?", "6th"),
    ("John Adams and Thomas Jefferson both died on the same date — what date?", "July 4, 1826 (50th anniversary of the Declaration of Independence)"),
    # Q1119: Golden Globes honor film and television
    ("The Golden Globe Awards are presented by which organization?", "Hollywood Foreign Press Association (HFPA)"),
    ("Golden Globes honor both film and TV — what major awards honor only film?", "Academy Awards (Oscars)"),
    # Q1120: Countries with larger population than US = 2 (China and India)
    ("What is the approximate current population of the United States?", "About 335 million"),
    ("China overtook India as the world's most populous country in 2023 — true or false?", "False — India surpassed China in 2023"),
    # Q1121: Lake Tahoe spans California and Nevada
    ("Lake Tahoe is the largest alpine lake in which country?", "United States (North America)"),
    ("What is Lake Tahoe known for in terms of its water?", "Exceptional clarity (you can see 75+ feet deep)"),
    # Q1122: Dred Scott = slave
    ("The Dred Scott decision was a famous US Supreme Court case from which year?", "1857"),
    ("What did the Dred Scott ruling declare about enslaved people?", "That they were not citizens and had no right to sue in federal court"),
    # Q1123: Dana White = CEO of UFC
    ("Dana White became president of UFC in 2001 under what ownership?", "Zuffa LLC (owned by the Fertitta brothers)"),
    ("In 2016, UFC was sold to which investment group for a record price?", "WME-IMG (Endeavor)"),
    # Q1124: Systolic = top blood pressure number
    ("What does the diastolic number (bottom) in blood pressure measure?", "Pressure in arteries when heart rests between beats"),
    ("Normal blood pressure is approximately what reading?", "120/80 mmHg"),
    # Q1125: Jason DeFord = Jelly Roll
    ("Jelly Roll is known for blending which two music genres?", "Country and hip-hop/rap"),
    ("Jelly Roll won which prestigious country music award in 2023?", "New Artist of the Year (CMA Awards)"),
    # Q1126: Kentucky Derby held in May
    ("The Kentucky Derby is called what by many horse racing fans?", "The Run for the Roses (because the winner is draped with roses)"),
    ("Where is the Kentucky Derby held?", "Churchill Downs in Louisville, Kentucky"),
    # Q1127: Drone = unmanned plane or male bee
    ("What is the role of a drone bee in a honeybee colony?", "To mate with the queen bee"),
    ("Drone aircraft that use AI are commonly called what?", "Autonomous drones or UAVs (unmanned aerial vehicles)"),
    # Q1128: Karate uniform = Gi (2 letters)
    ("What is the full Japanese name for a karate uniform?", "Karategi (or just gi)"),
    ("A judogi is the uniform worn in which martial art?", "Judo"),
    # Q1129: Arkansas River merges with Mississippi in Arkansas
    ("The Arkansas River originates in which US state?", "Colorado"),
    ("The Arkansas River is approximately how many miles long?", "About 1,469 miles (2,364 km)"),
    # Q1130: Golden State Warriors home = San Francisco
    ("Before moving to San Francisco, the Warriors played in which city?", "Oakland, California"),
    ("The Warriors play at which arena in San Francisco?", "Chase Center"),
    # Q1131: USA won most gold medals in 2024 Olympics
    ("Where were the 2024 Summer Olympics held?", "Paris, France"),
    ("How many gold medals did the USA win at the 2024 Paris Olympics?", "40 gold medals"),
    # Q1132: Lord of the Rings director = Peter Jackson
    ("Peter Jackson is from which country?", "New Zealand"),
    ("Which Lord of the Rings film won Best Picture at the Oscars?", "The Return of the King (2004)"),
    # Q1133: Person from Michigan = Michigander
    ("What is another acceptable term for a person from Michigan?", "Michiganian"),
    ("Abraham Lincoln coined the term 'Michigander' to mock which Michigan politician?", "General James Shields"),
    # Q1134: Russia's currency = Ruble
    ("What is the symbol for the Russian Ruble?", "₽"),
    ("The ruble has been Russia's currency since approximately which century?", "14th century"),
    # Q1135: Cleveland on Lake Erie
    ("Lake Erie is the shallowest and which-smallest of the Great Lakes?", "4th largest (second smallest by surface)"),
    ("Lake Erie is the most southern of the Great Lakes — true or false?", "True"),
    # Q1136: Crocodile has more pointed snout than alligator
    ("What is an easy way to distinguish a crocodile from an alligator?", "Crocodiles have a V-shaped snout; alligators have a U-shaped snout"),
    ("When a crocodile closes its mouth, which teeth are visible?", "Both upper and lower teeth (some lower teeth show)"),
    # Q1137: Only definite article in English = 'the'
    ("What are the indefinite articles in English?", "'a' and 'an'"),
    ("When do you use 'an' instead of 'a' as an indefinite article?", "Before words beginning with a vowel sound"),
    # Q1138: USS = United States Ship
    ("What does HMS stand for on British naval vessels?", "His/Her Majesty's Ship"),
    ("The most famous USS ship is arguably the USS Missouri — what class of battleship is it?", "Iowa class"),
    # Q1139: Beaver = herbivore
    ("What do beavers eat?", "Tree bark, leaves, roots, and aquatic plants"),
    ("Beavers are famous for building what structure?", "Dams (and lodges)"),
    # Q1140: Spell Daiquiri = D-A-I-Q-U-I-R-I
    ("The Daiquiri cocktail originated in which country?", "Cuba"),
    ("What are the three main ingredients in a classic Daiquiri?", "Rum, lime juice, and sugar"),
    # Q1141: Pulque traditional drink of Mexico (2000 years old)
    ("Pulque is made from the sap of which plant?", "Agave (maguey plant)"),
    ("What is pulque's alcohol content approximately?", "About 2-8% ABV"),
    # Q1142: River separating Minneapolis and St. Paul = Mississippi
    ("Minneapolis and St. Paul together are called what?", "The Twin Cities"),
    ("The Mississippi River originates in which US state?", "Minnesota (Lake Itasca)"),
    # Q1143: Extra dry martini = less vermouth
    ("What does a 'dry' martini mean?", "Less vermouth than usual"),
    ("What is a martini made with vodka instead of gin called?", "Vodka martini (or vodkatini)"),
    # Q1144: Farm animal with most young in a litter = pig
    ("How many piglets can a sow give birth to in a litter?", "Average 8-12, but up to 20+"),
    ("How many litters can a pig have per year?", "About 2 litters per year"),
    # Q1145: Highest possible poker hand = Royal Flush
    ("What cards make up a Royal Flush?", "Ace, King, Queen, Jack, and Ten — all of the same suit"),
    ("What is the probability of being dealt a Royal Flush in a 5-card poker hand?", "About 1 in 649,739"),
    # Q1146: Oldest person inaugurated as US President = Donald Trump
    ("How old was Donald Trump when he was inaugurated for the second time?", "78 years old"),
    ("Previously, who held the record as the oldest inaugural president?", "Joe Biden (78 years old when first inaugurated in 2021)"),
    # Q1147: First of Big Mac, Happy Meal, Egg McMuffin = Big Mac (1968)
    ("What year was the Happy Meal introduced?", "1979"),
    ("What year was the Egg McMuffin introduced?", "1972"),
    # Q1148: Vitamin from carrots = Vitamin A
    ("Vitamin A is found in carrots — what form of Vitamin A do carrots contain?", "Beta-carotene (which the body converts to Vitamin A)"),
    ("Vitamin A deficiency can cause what health problem?", "Night blindness (and other vision problems)"),
    # Q1149: Virginia is for lovers
    ("Virginia's 'Virginia is for Lovers' slogan was introduced in what decade?", "1969"),
    ("What is the capital of Virginia?", "Richmond"),
    # Q1150: Good Witch of the North in 1939 Wizard of Oz = Glinda
    ("In L. Frank Baum's original book, is Glinda the Good Witch of the North or South?", "South (in the book she is the Witch of the South; North in the movie)"),
    ("Who played Glinda in the 1939 film The Wizard of Oz?", "Billie Burke"),
    # Q1151: Cape Cod extends into Atlantic Ocean
    ("In which US state is Cape Cod located?", "Massachusetts"),
    ("Cape Cod is famous for which type of seafood?", "Lobster, clams, and cod"),
    # Q1152: 13th Amendment = abolition of slavery
    ("In what year was the 13th Amendment ratified?", "1865"),
    ("Which US president issued the Emancipation Proclamation before the 13th Amendment?", "Abraham Lincoln"),
    # Q1153: Amstel beer named after a river
    ("Amstel beer is brewed in which Dutch city?", "Amsterdam"),
    ("What is the largest beer company that owns Amstel Beer?", "Heineken"),
    # Q1154: Golden spike joining transcontinental railroad = Utah
    ("What city in Utah was the site of the golden spike ceremony?", "Promontory Summit (or Promontory Point), Utah"),
    ("In what year was the transcontinental railroad completed?", "1869"),
    # Q1155: Badger = omnivore
    ("What do badgers primarily eat?", "Earthworms, small mammals, insects, and plant matter"),
    ("What family of animals do badgers belong to?", "Mustelidae (same family as weasels, otters, wolverines)"),
    # Q1156: John Adams 2nd president = Federalist
    ("The Federalist Party is considered the predecessor to which modern party?", "Republican Party (though debated)"),
    ("Who were the primary leaders of the Federalist Party?", "Alexander Hamilton and John Adams"),
    # Q1157: Battle of Bull Run 1861 in Virginia
    ("There were two Battles of Bull Run — which side won both?", "Confederate forces"),
    ("The first Battle of Bull Run was also called what by Confederates?", "Battle of First Manassas"),
    # Q1158: US borders the Arctic Ocean
    ("Through which US state does the US share a border with the Arctic Ocean?", "Alaska"),
    ("The US actually has coasts on which four bodies of water?", "Atlantic Ocean, Pacific Ocean, Arctic Ocean, and Gulf of Mexico"),
    # Q1159: $25 chip in Las Vegas = green
    ("What color is a $5 chip in Las Vegas casinos?", "Red"),
    ("What color is a $100 chip in Las Vegas?", "Black"),
    # Q1160: Baby alligator = hatchling (9-letter word)
    ("How long is a baby alligator at birth?", "About 8-9 inches long"),
    ("American alligators are native to which two US states primarily?", "Florida and Louisiana"),
    # Q1161: Highest score without strikes in bowling = 190
    ("In bowling, what is a spare?", "Knocking down all 10 pins in two rolls"),
    ("What is a perfect score in bowling called, and what score is it?", "A 300 (perfect game)"),
    # Q1162: OPEC members = 12
    ("What does OPEC stand for?", "Organization of the Petroleum Exporting Countries"),
    ("OPEC was founded in what year?", "1960"),
    # Q1163: Continents entirely in Southern Hemisphere = 1 (Antarctica)
    ("What two continents are mostly in the Southern Hemisphere (but not entirely)?", "South America and Australia/Oceania"),
    ("What is the southernmost continent?", "Antarctica"),
    # Q1164: Sluice used by miners
    ("What is a sluice used for in mining?", "To separate gold or heavy minerals from gravel using flowing water"),
    ("What type of gold mining uses a sluice box?", "Placer mining (alluvial gold mining)"),
]

# Build questions_plus.json
result = []
for i, q in enumerate(questions):
    result.append({"session": q["session"], "question": q["question"], "answer": q["answer"], "type": "original"})
    c1 = challenges[i*2]
    c2 = challenges[i*2+1]
    result.append({"session": q["session"], "question": c1[0], "answer": c1[1], "type": "challenge", "related_to": i})
    result.append({"session": q["session"], "question": c2[0], "answer": c2[1], "type": "challenge", "related_to": i})

with open('/home/claude/pub-trivia/questions_plus.json', 'w') as f:
    json.dump(result, f, indent=2)
print(f"Written {len(result)} entries to questions_plus.json")
