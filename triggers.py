#Specific Keyword Response
trigger_dictionary = {
    ("hit-n-run", "driver","run over","driver"): ["My driver, {}, was driving the car when the mishap occurred","Aap devil ke peeche, devil aapke peeche - too much fun!","Badminton court jao, tennis court jao, food court jao... lekin woh court mat jaana"],
    ("black buck","blackbuck", "deer", "poaching"): ["Dosti ka ek usool hai madam - no black buck, no jail", "Mere baarein mein itna mat sochna. Court mein aata hoon Jail mein nahi", "Tujhe har goli ka hisaab dena parta hai... main jitni bhi chalaon... mujhe koi hisaab nahin dena parta"],
    ("lulia", "katrina", "aish", "aishwarya", "jacqueline"): ["Our business is our business, none of your business","Mujhe toh nihayati khurrat plus kamini honhaar biwi chahiye", "99% ladkiyo ko unka mann pasand ladka mil jaata hai. lekin 99%% ladko ko unki pasand ki ladkiya kabhi nahi milti", "Neeli chatri waale, agar tu hai toh meri fariyad sun. Is duniya mein kahi ladkiyan hai... ek toh, arre ek toh mere liye chun"]
}


#Random Response
quotes = ["Boyfriend Girlfriend Se Darta Hai,  Girlfriend Cockroach Se Darti Hai,  Cockroach Chuhe Se Darta Hai,  Chuha Billi Se Darta Hai,  Billi Kutte Se Darti Hai,  Aur Kutta Aadmi Se Darta Hai...  Aur Aadmi Aurat Se Darta Hai...  Vaise Hi Jaise Villain Hero Se Darta Hai",
"Dosti ki hai, nibhani toh padegi",
"Hum tum mein itne ched karenge ki confuse ho jaoge ki saans kahan se le aur paadein kahan se",
"Mujhpe ek ehsaan karna, mujhpe koi eshaan mat karna",
"Ek baar maine commitment kardi toh phir mein black buck ki bhi nahi sunta",
"Zindagi mein teen cheezein kabhi underestimate nahi karna - mera driver, {} aur black buck",
"Saala main bhi pheku aur yeh bhi pheku. Circus ka retired black buck lagta hai",
"Hum Bajrangbali ke bhakt hain. Mar jayenge lekin jhooth nahi bolenge",
"Mere baarein mein itna mat sochna. Dil mein aata hoon samajh mein nahi",
"Aap devil ke peeche, devil aapke peeche - too much fun!",
"Swagat nahi karoge aap humara?",
"Abbe hool de raha hai? Muscle dekha hai muscle? Masal ke rakh doonga!",
"He never bites. He only loves.",
"Agar tum mujhe yunhi dekhti rahi toh tumhe mujhse pyaar ho jayega",
"Jab tum hasti ho toh tum bahut khubsoorat lagti ho. You look very ugly.",
"Abbe tu Sunny hai, Sunny Deol nahin.",
"Jahan Lad-Ka Aur Lad-Ki Ho...  Wahan Lad-Na Toh Hoga Hi Na",
"Aaisa Gayab Kar Doonga Ki Google.Com Bhi Tumhe Dhoond Na Payega",
"(Takes off the coat) (Rolls up the sleeves)",
"Yeh show aapke layak hai nahi, please leave my home",
"**MAI AA JAU KYA APNI PAR!**",
"Dude! {}!!! hadd mei rehna mere saath! You don't try what you try inside, with me!.. Ye kya hai? Time Out kya hai? Ye kisse baat kar rahe ho?",
"Sirf ek hi aadmi real lag raha hai yaha par, aur wo hai {}",
"{} you are doing really well. Jab sub me ghuse the tab beautiful man and now you are looking like a he-man. Everyone is really proud of you.",
"*Do whatever you want to do man. Do double, but don't trouble your mother man*",
"Kabhi toh stand liya karo",
"Log kehte hai khoobsurat ladkiyan jab jhoot bolti hai... toh aur bhi khoobsurat lagti hai",
"*Agar mujhe malum hota ki mujhe dekhkar tumhare chehre pe hazaar watt ki muskaan phail jati... toh main kab ka aa chuka hota*",
"Sari duniya pyar mein padi hui hai... sirf ek mujhe hi haq nahi hai?... ki main kisi se pyar kar sakun, koi mujhse pyar kar sake... kyun?",
"Udaas hona, yun akele mein rona... is injurious to health, sehat ke liye hanikarak hota hai",
"Bahut goor raha hai... kya behen ki shaadi karayega muhjse?",
"*Sharab aur khoon main apni marzi se peeta hoon ... dabake*",
"Aam aadmi sota hua sher hai... ungli mat kar... jaag gaya toh cheer phaad dega",
"Main request nahi karta... ek hi baar bolta hoon... aur full and final ho jaata hai",
"Jis school mein tune ye sab seekha hai na... uska headmaster aaj bhi mujhse tuition leta hai",
"Dosti ka ek oosul hai madam... no sorry, no thank you",
"*Chehre par gussa, mann mein gaali... goli bhi chalali... phir bhi dono haath khali*",
"Badtameez, chaddar ki kameez, lohe ka pajama, bandar tera mama, arre billi teri mausi, kutta tera yaar, aam ka achaar... aaja mere yaar!",
"*Woh jeena bhi koi jeena hai jis mein kick na ho*",
"Gulab jamun se yaad aaya... {} ji aapke hernia ka operation hone waala tha?",
"Yahi toh baat mujhe aapki bahut achchi lagti hai... ki aapko kuch samajh mein hi nahi aata",
"Hum yahan ke Robinhood hai... Robinhood Pandey",
"Aap thank you mat kahiye... instead teen logon ki madad ki jiye aap... aur un teeno se kehna ki woh teen aur ki madad karen... duniya badal jayegi",
"Abhi tak sabko nehlaya hai... ab sabko dhounga",
"Waqt tumhara kharab aaya hai aur din hum gine",
"*Suar hamesha group mein shikaar karte hai... aur sher akele*",
"Mujhe khud ko bhi nahin pata... ki kitna kamina hoon main",
"Mujhse joh dushmani modh leta hai... uspe uparwaala reham toh kar deta hai, magar main nahi",
"Meri ek khasiyat hai ki main maarta kam hoon... aur ghaseet-ta zyada hoon",
"Sudhar jao... varna agar hum sudhaarne par utar aaye... toh bahut nuksaan ho jayega",
"Aaj ke baad agar tune mere dost ki taraf aankh bhi uthakar dekha... toh Yamuna mein pani nahi... tera khoon bahega",
"Mujhe aasoonyon se sakt allergy hai!",
"Saari shikayatein ek saath likhva dijiye... mooch, shirt, tie, pant, underwear, banyan, kuch mat chhodiye... dhajjiyan udha dijiye... lekin pyar nahi karta, yeh mat likhvaiye",
"*Shikaar toh sab karte hai, lekin tiger se behtar shikaar koi nahi karta!*",
"Utna hi maaro, jitna ki khud bardaash kar sako",
"Abhe kaika tu yaar... bhaad mein gaya tera pyar",
"Akal ke aane ke liye shakal ke bighadneka kyun intezar kar rahe the tum?",
"*Tu kaam karta gaya, main ishq karta gaya... tera naam hota gaya, main badnaam hota gaya*",
"Jis race se mujhe nikaalne ki baat kar rahe hai yeh bewakoof... woh nahi jaante hai... us race ka sikandar main hoon",
"Arre kaka main toh kaka ban gaya",
"Yeh thopade ka design toh pehli baar dekh raha hoon!",
"Tumhari aankhon se tumhara dil dikhta hai. Jis mein meri tasveer chupi hui hai",
"Main modern zamane ka kutta hoon... wooow wooow wooow",
"*Yeh race zindagi ki race hai. Kisi ki zindagi leke hi khatam hogi*",
"Dil mein aata hoon samajh mein nahi... pant mein aata hoon shirt mein nahi... cycle pe aata hoon gaadi mein nahi... aur sun langoth mein aata hoon shorts mein nahi",
"Abhe main un mein se hoon, joh machli ko doobo ke maar sakta hoon!",
"I am a bad boy.. Thoda sa ziddi, thoda sa awara, thoda sa pagal, thoda sa nakara... yani total milake I am a bad boy.",
"Main characterless zaroor hoon... lekin itna bhi less nahi!",
"Main yahan rishtey jodne aaya hoon... haddiyan todne nahi",
"Tu Superman hai?... Spiderman hai?... abhe tu common man hai",
"*Hum unhi ko thokte hai joh ke zaroorat se zyada bhaukte hai*",
"Pehle samjhao baat... nahi samajh mein aaya... toh do kheench ke laat!",
"Jiske paas family support hai... usse koi deport nahi kar sakta",
"Yeh toh mafia ke baap hai... ek nevla toh doosra saanp hai... agar dono mil jaaye toh killer shark hai... lekin dono angootha chaap hai",
"*Haste huye chehre ka gham padhna kitna mushkil hota hai.*",
"Bina kuch kiye lene ke dene padh rahe hai... agar kuch by chance kar liye toh lene aur dene dono padh jayenge",
"Badminton court jao, tennis court jao, food court jao... lekin woh court mat jaana!!",
"{}, iss hafte aisa koi bhi incident bataiye jaha par aapne Archana ka saath diya ho?",
"Aap sabko batana hai ke kis sadasya ki konsi galat fehmi hai, aur unka ek gubbara phodna hai. Start kijiye {0} se, Accha Yeh nahi keh sakte ki {0} khud ek galat fehmi hai!",
"Kya permission doon mein? Isko jaan se maar dalo!!!",
"Tell me straight out honestly, ya ye sirf mujhe hi dikhai de raha hai ke {} is obsessed with Shalin!",
"Ek baat mein clear karna chah raha hu ke sabka khayal rakha jaa raha hai, aur team ko ya biggboss ko koyi shauk nahi hai biased hone ka.",
"{} ye to ek bada hi ajeeb sa mamla ho gaya yaha par ke, aap iss sub ke andar dikh nahi rahe ho lekin logon ki baaton mein aapka zikr ho raha hai!",
"Aapne hospital ka bahana lekar apni bacchi se baat karne ki khoshih ki hai!",
"Humein iss prakar ka content nahi chahiye!"]