import re
import pandas as pd

# Sample text data
text_data = """
1	Sunkavilli Suranya
17PA1A04F2
Palo Alto Networks	
 
2	Manne Tejaswini Sri Naga Sai
17PA1A0592
Amazon.	
 
3	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
Amazon.	
 
4	Nittala Lakshmi Sudeepthi
17PA1A05B5
Amazon	
 
5	Gopisetti Lahari
17PA1A0545
Amazon	
 
6	Kothagundu Venkata Krishna Rao
17PA1A0579
Cleartrip	
 
7	Eada Kamal Tej Reddy
17PA1A0532
Cleartrip	
 
8	Koppuravuri Dakshayani Manozna
17PA1A0578
Flipkart	
 
9	Jampana Sri Guru Vyshnavi
17PA1A0557
BNY Mellon	
 
10	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
BNY Mellon	
 
11	Bandi Likhitha Ramalakshmi
17PA1A0511
Pega Systems	
 
12	Miriyala Vihari
17PA1A0497
Pega Systems	
 
13	Chakka Neha
17PA1A0418
Pega Systems	
 
14	Sanku Madhu Venkata Naga Yesu
17PA1A04E2
Byjus	
 
15	Achant Yesuratnam
17PA1A0301
Byjus	
 
16	Borusu Teja Rajesh
17PA1A0313
Byjus	
 
17	Kokkirala Dinesh Venkata Sai
17PA1A0462
Delta VRobo	
 
18	Dasireddy Anusha
17PA1A1209
State Street	
 
19	Gannamani Siva Sankar
17PA1A0537
State Street	
 
20	Malakala Sai Venkatesh
17PA1A0365
Quantiphi Analytics solutions pvt ltd	
 
21	Tammineedi Usha Naga Sri
17PA1A05F4
Athena Health	
 
22	Shaik Ashwah
17PA1A05E7
OpenText	
 
23	Mopidevi Purna
17PA1A0499
Infosys PP(Through InfyTQ)	
 
24	Jampana Sri Guru Vyshnavi
17PA1A0557
NCR	
 
25	Kallepalli Shalini
17PA1A0564
Delhivery	
 
26	Nittala Lakshmi Sudeepthi
17PA1A05B5
Delhivery	
 
27	Jampana Sri Guru Vyshnavi
17PA1A0557
Delhivery	
 
28	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
Infosys PP(Through HackWithinfy)	
 
29	Garaga Yathish Bhargav
17PA1A0538
Infosys PP(Through HackWithinfy)	
 
30	Gopisetti Lahari
17PA1A0545
Infosys PP(Through HackWithinfy)	
 
31	Appada Aravinda Prakash
17PA1A1202
Netcore Cloud Private Limited	
 
32	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
Micron	
 
33	Nekkalapudi Basanth
17PA1A1236
TCS Codevita - Digital	
 
34	Katta Monika
17PA1A0569
TCS Codevita - Digital	
 
35	Magapu Jahnavi Devi
17PA1A0485
TCS Codevita - Digital	
 
36	Manam Narayana Rao
17PA1A0487
Wiley mThree	
 
37	Poduri Mohana Sri Sai Vamsi
17PA1A04D1
Vodafone(Pega)	
 
38	Grandhi Sri Ram
17PA1A0549
JP Morgan	
 
39	Adda Teja
17PA1A0403
Morgan Stanley	
 
40	Karri Surya Teja
17PA1A0568
Accolite	
 
41	Valavala Saiswetha
17PA1A1256
Morgan Stanley	
 
42	Nangineedi Naresh Babu
17PA1A1234
TCS Digital(Through upgrade Test)	
 
43	Ravi Naveen Sai Tanay
17PA1A05D4
TCS NQT - Digital	
 
44	Penugonda Naga Venkata Raviteja
17PA1A05C6
TCS NQT - Digital	
 
45	Kothagundu Venkata Krishna Rao
17PA1A0579
TCS NQT - Digital	
 
46	Kayala Sai Vamsi
17PA1A0570
TCS NQT - Digital	
 
47	Eada Kamal Tej Reddy
17PA1A0532
TCS NQT - Digital	
 
48	Sunkavilli Suranya
17PA1A04F2
TCS NQT - Digital	
 
49	Veerni Sai Venkata Durga Asish
17PA1A04H1
TCS NQT - Digital	
 
50	Kokkirala Dinesh Venkata Sai
17PA1A0462
TCS Digital(Through upgrade Test)	
 
51	Ravuri Yazneswara Ram Charan
17PA1A03A1
TCS NQT - Digital	
 
52	Abburi Pavani
17PA1A0201
TCS NQT - Digital	
 
53	Chinni Alekhya
17PA1A0522
Accolite	
 
54	Manne Tejaswini Sri Naga Sai
17PA1A0592
Accolite	
 
55	Sunkavilli Suranya
17PA1A04F2
Accolite	
 
56	Kayala Sai Vamsi
17PA1A0570
Accolite	
 
57	Velaga Sushma
17PA1A05G9
TCS Digital(Through upgrade Test)	
 
58	Neduri Veera Venkata Ram Pandu
17PA1A05B1
TCS Digital(Through upgrade Test)	
 
59	Jampana Sri Guru Vyshnavi
17PA1A0557
TCS Digital(Through upgrade Test)	
 
60	Manam Narayana Rao
17PA1A0487
TCS Digital(Through upgrade Test)	
 
61	Kanteti Janardhana Gupta
17PA1A0457
TCS Digital(Through upgrade Test)	
 
62	Nulu Jagadeesh Gupta
17PA1A0267
TCS Digital(Through upgrade Test)	
 
63	Govada Srinivasa Rao
18PA5A0409
Legato Health(Pega)	
 
64	Mallina Venkata Kishore
17PA1A0589
JP Morgan	
 
65	Bellamkonda Rohin Surya Prakash
17PA1A1205
IVY Tech	
 
66	Vanapalli Sridevi
17PA1A05G3
IVY Tech	
 
67	Sayyed Hussain
17PA1A05E4
IVY Tech	
 
68	Irrinki Neelima Devi
17PA1A0554
IVY Tech	
 
69	Parikela Moni Adithya
17PA1A05C4
IVY Tech	
 
70	Bezawada Sadhvi
17PA1A0512
IVY Tech	
 
71	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
Capgemini-Diff	
 
72	Penugonda Naga Venkata Raviteja
17PA1A05C6
Capgemini-Diff	
 
73	Sunkavilli Suranya
17PA1A04F2
Capgemini-Diff	
 
74	Jeji Srinivasa Vinnakota
17PA1A0446
Capgemini-Diff	
 
75	Adabala Mahesh Babu
17PA1A0402
Capgemini-Diff	
 
76	Pamoti Vasudeva Manikanta
18PA5A0220
Zoho	
 
77	Kusumanchi Lakshmi Mani Deepika
17PA1A0583
Zoho	
 
78	Kone Srimannarayana
17PA1A0577
Zoho	
 
79	Neduri Veera Venkata Ram Pandu
17PA1A05B1
Zoho	
 
80	Narina Tharaka Sai Ram
17PA1A05B0
Zoho	
 
81	Kolla Ravi Teja
17PA1A0571
Zoho	
 
82	Pasumarthi Harsha Vardhan
17PA1A04C4
Zoho	
 
83	Annepu Sahasra
17PA1A0507
SOTI	
 
84	Irrinki Neelima Devi
17PA1A0554
Accenture Elite	
 
85	Mudunuri Meher Krishna Varma
17PA1A0261
Planet Spark	
 
86	Puli Sai Swetha
17PA1A0146
Planet Spark	
 
87	Gundabathula Anusha
17PA1A0232
Planet Spark	
 
88	Peeta Manideep Sai
18PA5A0320
Planet Spark	
 
89	Adda Teja
17PA1A0403
Planet Spark	
 
90	Kaddala Siva Kumar
17PA1A0560
Infosys.	
 
91	Pala Manoj Kumar
18PA5A0230
Landys+Gyr	
 
92	Mulagapati Sasank Siddhardha
18PA5A0510
SkillVertex	
 
93	G Monisha
17PA1A0535
PWC	
 
94	Choragudi Sai Praveen
17PA1A0524
EPAM	
 
95	Kusumanchi Lakshmi Mani Deepika
17PA1A0583
EPAM	
 
96	Kone Srimannarayana
17PA1A0577
EPAM	
 
97	Vasamsetti Satyendra Prasad
17PA1A05G6
EPAM	
 
98	Nekkalapudi Rama Lakshmi
17PA1A1237
EPAM	
 
99	Sadhanala Satya Sai Srivalli
17PA1A05D6
EPAM	
 
100	Kallepalli Shalini
17PA1A0564
EPAM	
 
101	Nimmadhi Jyohi Naga Venkata Siva Sairam
17PA1A05B4
EPAM	
 
102	Eada Kamal Tej Reddy
17PA1A0532
EPAM	
 
103	Veerni Sai Venkata Durga Asish
17PA1A04H1
EPAM	
 
104	Anguluri Krupa Jessica
17PA1A0506
EPAM	
 
105	Magapu Jahnavi Devi
17PA1A0485
EPAM	
 
106	Madeti Pavani N S S M K Priyanka
17PA1A0484
EPAM	
 
107	Bandarupalli Sri Venkata Sai Gopi Anand
17PA1A0411
Immovidu Technologies	
 
108	Sri Krishna Chaitanya Varma D
18PA5A0224
LatentView	
 
109	Penugonda Naga Venkata Raviteja
17PA1A05C6
Eazydiner	
 
110	Satyavolu Venkat Sai Charan
17PA1A0288
Presidio	
 
111	Pamoti Vasudeva Manikanta
18PA5A0220
Presidio	
 
112	Velaga Sushma
17PA1A05G9
Seneca Global	
 
113	Vanapalli Sridevi
17PA1A05G3
Seneca Global	
 
114	Dirisala Lavanya
17PA1A0531
Seneca Global	
 
115	Chinni Chaithanya
17PA1A0317
Seneca Global	
 
116	Padarthi Rangarao
17PA1A05B9
Publicis sapient	
 
117	Vasukuri Naga Venkata Satish
18PA5A0434
UHG(Pega)	
 
118	Gadamsetty Mohith
18PA5A0407
UHG(Pega)	
 
119	Nalla Kishore
17PA1A1232
UHG(Pega)	
 
120	Swarna Sai Prasanka
17PA1A05F2
UHG(Pega)	
 
121	Vegi Bhanu Adinarayana
17PA1A04H2
UHG(Pega)	
 
122	Ummadi Satya Jai Deep
17PA1A04G2
UHG(Pega)	
 
123	Narra Manohar
17PA1A04B2
UHG(Pega)	
 
124	Kotikalapudi Phaneendra
17PA1A0475
UHG(Pega)	
 
125	Penugonda Naga Venkata Raviteja
17PA1A05C6
Infosys SES(Through InfyTQ)	
 
126	Choragudi Sai Praveen
17PA1A0524
Infosys SES(Through InfyTQ)	
 
127	Nangineedi Naresh Babu
17PA1A1234
Infosys SES(Through HackWithinfy)	
 
128	Sunkara Pavan Kalyan Ayyappa
17PA1A05F1
Infosys SES(Through HackWithinfy)	
 
129	Ravi Naveen Sai Tanay
17PA1A05D4
Infosys SES(Through HackWithinfy)	
 
130	Nukala Y Ch Mani Rama Naidu
17PA1A05B6
Infosys SES(Through HackWithinfy)	
 
131	Narina Tharaka Sai Ram
17PA1A05B0
Infosys SES(Through HackWithinfy)	
 
132	Valavala Saiswetha
17PA1A1256
Infosys SES(Through HackWithinfy)	
 
133	Vanapalli Sridevi
17PA1A05G3
Infosys SES(Through HackWithinfy)	
 
134	Tumpudi Murali Sai Kamal Srikanth
17PA1A05G1
Infosys SES(Through HackWithinfy)	
 
135	Nimmadhi Jyohi Naga Venkata Siva Sairam
17PA1A05B4
Infosys SES(Through HackWithinfy)	
 
136	Kusumanchi Lakshmi Mani Deepika
17PA1A0583
Infosys SES(Through HackWithinfy)	
 
137	Kone Srimannarayana
17PA1A0577
Infosys SES(Through HackWithinfy)	
 
138	Kayala Sai Vamsi
17PA1A0570
Infosys SES(Through HackWithinfy)	
 
139	Dammuluri Yogendra Sai Teja
17PA1A0421
Infosys SES(Through HackWithinfy)	
 
140	Syed Kareem Siraz
17PA1A0294
Infosys SES(Through HackWithinfy)	
 
141	Pulagam Sai Venkata Krishna
17PA1A0277
Infosys SES(Through HackWithinfy)	
 
142	Kolla Ravi Teja
17PA1A0571
Infosys SES(Through HackWithinfy)	
 
143	Jampana Sri Guru Vyshnavi
17PA1A0557
Infosys SES(Through HackWithinfy)	
 
144	Garapati Bulli Ramesh
17PA1A0539
Infosys SES(Through HackWithinfy)	
 
145	Gubbala Vivek
17PA1A0331
Infosys SES(Through HackWithinfy)	
 
146	Chinni Alekhya
17PA1A0522
Infosys SES(Through HackWithinfy)	
 
147	Nittala Lakshmi Sudeepthi
17PA1A05B5
Infosys SES(Through HackWithinfy)	
 
148	Padarthi Rangarao
17PA1A05B9
Bosch	
 
149	Metla D N V S S M Sri Harsha
17PA1A0496
Cognizant	
 
150	Kopparthi Vara Lakshmi
17PA1A1222
Accenture	
 
151	Gutla Dileep Kumar
18PA5A0309
Accenture	
 
152	Govada Srinivasa Rao
18PA5A0409
Coforge(Pega)	
 
153	Tamarapalli Naga Vamsi Santhosh
17PA1A04F4
Coforge(Pega)	
 
154	Penmetsa Satish Varma
17PA1A04C9
Coforge(Pega)	
 
155	Nachu N D V Prasad
17PA1A1231
Cognizant	
 
156	Tirumala Bhaskara Durga Naga Pavan Kalyan
18PA5A0517
Cognizant	
 
157	Chintapalli Krishna Mohan
18PA5A0503
Cognizant	
 
158	Borra Surya Nagendra Gowda
18PA5A0404
Cognizant	
 
159	Shaik Abdul Malik
18PA5A0324
Cognizant	
 
160	Vaddimukkala Rahul
18PA5A0227
Cognizant	
 
161	Tirumala Sai Sandeep
18PA5A0231
Cognizant	
 
162	Madepalli V V D G Sivanagu
18PA5A0218
Cognizant	
 
163	Upputuri Bhanu Kalyan
17PA1A1255
Cognizant	
 
164	Jalaparthi Rani
17PA1A1216
Cognizant	
 
165	Kudupudi Rajesh Kumar
17PA1A1224
Cognizant	
 
166	Appada Aravinda Prakash
17PA1A1202
Cognizant	
 
167	Vanapalli Sridevi
17PA1A05G3
Cognizant	
 
168	Sayyed Hussain
17PA1A05E4
Cognizant	
 
169	G Monisha
17PA1A0535
Cognizant	
 
170	Kondeti Lokesh
17PA1A0576
Cognizant	
 
171	Didla Vijay Stalin Babu
17PA1A0530
Cognizant	
 
172	Vasa Uday Kiran
17PA1A04G8
Cognizant	
 
173	Muthyala T V Kishore Babu
17PA1A04A7
Cognizant	
 
174	Bandarupalli Sri Venkata Sai Gopi Anand
17PA1A0411
Cognizant	
 
175	Poduri Teja Naga Raju
17PA1A0393
Cognizant	
 
176	Lanka Satya Prasad
17PA1A0362
Cognizant	
 
177	Kandukuri Anudeep
17PA1A0349
Cognizant	
 
178	Yetukuri Sandeepvarma
17PA1A02B5
Cognizant	
 
179	Ram Charan Pechetti
17PA1A0280
Cognizant	
 
180	Nakkani Naga Devi Apparao
17PA1A0264
Cognizant	
 
181	Mudunuri Meher Krishna Varma
17PA1A0261
Cognizant	
 
182	Kalla Sreeram
17PA1A0239
Cognizant	
 
183	Kurmasala Sai Kishore
17PA1A0252
Cognizant	
 
184	Akurathi Nikhil
17PA1A0203
Cognizant	
 
185	Puli Sai Swetha
17PA1A0146
Cognizant	
 
186	Nammi Venkata Balamurali
17PA1A05A8
Cognizant	
 
187	Kokkirala Dinesh Venkata Sai
17PA1A0462
Cognizant	
 
188	Yalamanchili Phani Sai Manojahar
17PA1A04H6
Accenture	
 
189	Kothari Balu Phanendra
18PA5A0508
Accenture	
 
190	Maddala Venkatesh
18PA5A0417
Accenture	
 
191	Jedda Anilkumar
18PA5A0312
Accenture	
 
192	Battula Deepak Raj
18PA5A0303
Accenture	
 
193	Guttula Jaya Balaji
18PA5A0213
Accenture	
 
194	Dasari Ravi Chandra
18PA5A0210
Accenture	
 
195	Kadiyam Nandini
17PA1A1218
Accenture	
 
196	Pappala Tharun Sai Naidu
17PA1A05C3
Accenture	
 
197	Bellamkonda Rohin Surya Prakash
17PA1A1205
Accenture	
 
198	Padarthi Rangarao
17PA1A05B9
Accenture	
 
199	Mohammed Nadeem
17PA1A0598
Accenture	
 
200	Karri Surya Teja
17PA1A0568
Accenture	
 
201	Grandhi Sri Ram
17PA1A0549
Accenture	
 
202	Godavarthi Sri Sai Sruthi
17PA1A0543
Accenture	
 
203	Chakka Vishnu Satya Raghu Vamsi
17PA1A0518
Accenture	
 
204	Bezawada Sadhvi
17PA1A0512
Accenture	
 
205	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
Accenture	
 
206	Piridi Someswara Sai Kumar
17PA1A04D0
Accenture	
 
207	Palleti Krupa Sravanthi
17PA1A04B9
Accenture	
 
208	Kundula P S S N V Ravi Kumar
17PA1A0476
Accenture	
 
209	Lankalapilli Sowmya
17PA1A0481
Accenture	
 
210	Jagarlamudi Mohana Naresh
17PA1A0443
Accenture	
 
211	Garapati Lakshmi Veera Venkata Sairamkumar
17PA1A0430
Accenture	
 
212	Bandarupalli Sri Venkata Sai Gopi Anand
17PA1A0411
Accenture	
 
213	Vanga Sai Kondala Satwik
17PA1A03B2
Accenture	
 
214	Navadu Leela Venkata Gowtham Krishna
17PA1A0382
Accenture	
 
215	Musini Siva Krishna Kanth
17PA1A0378
Accenture	
 
216	Bande Nanda Kishore
17PA1A0307
Accenture	
 
217	Valluri Jaswanth
17PA1A02A5
Accenture	
 
218	Pulagam Sai Venkata Krishna
17PA1A0277
Accenture	
 
219	Pedapati Balaram Sandeep
17PA1A0272
Accenture	
 
220	Nalla Venkata Sai Ram Mohan
17PA1A0266
Accenture	
 
221	Nakkani Naga Devi Apparao
17PA1A0264
Accenture	
 
222	Mudunuri Meher Krishna Varma
17PA1A0261
Accenture	
 
223	Chinnamsetty Anilkumar
17PA1A0218
Accenture	
 
224	Devarapu Vishnu Sai Sri Nataraj
17PA1A0223
Accenture	
 
225	Shaik Pavan Kumar
17PA1A0152
Accenture	
 
226	Motupalli Krishna Chaitanya
17PA1A0134
Accenture	
 
227	Kothari Balu Phanendra
18PA5A0508
Persistent	
 
228	Badeti Pardha Saradhi
18PA5A0502
Persistent	
 
229	Puli Sai Swetha
17PA1A0146
Accenture	
 
230	Kurmala Sri Lakshmi Sravani
17PA1A0129
Accenture	
 
231	Ravada Vinay Kumar
18PA5A0323
Accenture	
 
232	Danduprolu Ayyappa Vardhan
18PA5A0306
Accenture	
 
233	Darabattula Sandeep
18PA5A0209
Accenture	
 
234	Patcha Gowri Prathyusha Bhavani
17PA1A1245
Accenture	
 
235	Penmetsa Shanmitha Pooja
17PA1A1246
Accenture	
 
236	Munukoti Sai Sri Hari Chandana
17PA1A1230
Accenture	
 
237	Lokam Jhnana Reshmika
17PA1A1225
Accenture	
 
238	Mopidevi Jyothsna Devi
17PA1A1229
Accenture	
 
239	Juveriya Tasneem
17PA1A1217
Accenture	
 
240	Datla Annapurna
17PA1A1210
Accenture	
 
241	Sheik Sharuk
17PA1A05F0
Accenture	
 
242	Nelluri Yamini Lakshmi Tirupathamma
17PA1A04B5
Accenture	
 
243	Annepu Sahasra
17PA1A0507
Coforge(Pega)	
 
244	Bachu Eswar
17PA1A0408
Coforge(Pega)	
 
245	Penchikalapati Veera Bhupathi Dev
18PA5A0512
Coforge(Pega)	
 
246	Kadulla Swathi
18PA5A0412
Coforge(Pega)	
 
247	Amujala Bhavana
17PA1A1201
Coforge(Pega)	
 
248	Gadamsetty Mohith
18PA5A0407
Coforge(Pega)	
 
249	Yalamati Rohini
17PA1A05H1
Coforge(Pega)	
 
250	Yadlapalli P G Narasimha Rao
17PA1A05H0
Coforge(Pega)	
 
251	Seelamsetti V N Sindhu Sha
17PA1A05E5
Coforge(Pega)	
 
252	Sarede Jagadhiswari
17PA1A05E2
Coforge(Pega)	
 
253	Ponnaganti Vasantha Lakshmi
17PA1A05D0
Coforge(Pega)	
 
254	Pallantla Devendrakumar
17PA1A05C2
Coforge(Pega)	
 
255	Mallela Praveen
17PA1A0588
Coforge(Pega)	
 
256	Likhithapudi Noel
17PA1A0584
Coforge(Pega)	
 
257	Gurram Anand Paul
17PA1A0551
Coforge(Pega)	
 
258	Grandhi Himavarshini
17PA1A0548
Coforge(Pega)	
 
259	Goriparthi Anvitha
17PA1A0547
Coforge(Pega)	
 
260	Chitturi Keerthana
17PA1A0523
Coforge(Pega)	
 
261	Bandi Likhitha Ramalakshmi
17PA1A0511
Coforge(Pega)	
 
262	Alluri Vishnu Vardhan Varma
17PA1A0505
Coforge(Pega)	
 
263	Shaik Asha
17PA1A04E5
Coforge(Pega)	
 
264	Sai Madhuri Kappaganthula
17PA1A04E1
Coforge(Pega)	
 
265	Poshala Praneeth Goud
17PA1A04D3
Coforge(Pega)	
 
266	Mullapudi Sai Prapoorna
17PA1A04A5
Coforge(Pega)	
 
267	Miriyala Vihari
17PA1A0497
Coforge(Pega)	
 
268	Mekala Mohanvenkat Sai
17PA1A0494
Coforge(Pega)	
 
269	Madana Venkata Nagasai Phanipavan
17PA1A0482
Coforge(Pega)	
 
270	Komatlapalli Sai Teja
17PA1A0464
Coforge(Pega)	
 
271	Kamuju Navya Supriya
17PA1A0455
Coforge(Pega)	
 
272	Indukuri Sai Viswanath Varma
17PA1A0439
Coforge(Pega)	
 
273	Bonam Kiran Teja
17PA1A0416
Coforge(Pega)	
 
274	Nerella Naga Venkata Navya
17PA1A1239
Accenture(Pega)	
 
275	Gudapati Pavan Sumanth
17PA1A0436
Accenture(Pega)	
 
276	Battula Deepak Raj
18PA5A0303
Cognizant	
 
277	Sadanala Gana Satya Sai Rajesh
17PA1A0148
Cognizant	
 
278	Piridi Someswara Sai Kumar
17PA1A04D0
Cognizant	
 
279	Undapalli Venkata Reddy Naidu
18PA5A0518
Cognizant	
 
280	Kandikatla Aishwarya Robin
17PA1A1219
Accenture	
 
281	Kudupudi Rajesh Kumar
17PA1A1224
Accenture	
 
282	Supriya Rani Medidi
17PA1A0292
Accenture	
 
283	Sadanala Gana Satya Sai Rajesh
17PA1A0148
Accenture	
 
284	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
Vodafone	
 
285	Giri Surya Kiran Padavala
17PA1A0542
Cognizant	
 
286	Akumarthi Karun Kumar
18PA5A0202
ALCHEMY TECHSOL INDIA PVT.LTD.	
 
287	Boyedi Shanthi Kumar
17PA1A0516
Accenture	
 
288	Geddam Akhil
17PA1A0541
Cognizant	
 
289	Kothapalli Prasannakumar
17PA1A0474
Cognizant	
 
290	Kota Venkata Satya Avinash
17PA1A0473
Infosys(Pega)	
 
291	Shaik Naseema
17PA1A04E6
Infosys(Pega)	
 
292	Manda Sai Sri
17PA1A0488
Infosys(Pega)	
 
293	Mohammad Ayeshma
17PA1A1228
LTI(Pega)	
 
294	Gunnam Surya Krishna
18PA5A0410
LTI(Pega)	
 
295	Sagiraju Somesh Datta Varma
17PA1A05D7
LTI(Pega)	
 
296	Poduri Mohana Sri Sai Vamsi
17PA1A04D1
LTI(Pega)	
 
297	Shaik Afroz Fathima
17PA1A04E4
LTI(Pega)	
 
298	Chakka Neha
17PA1A0418
LTI(Pega)	
 
299	Dusari Srikanth
17PA1A1212
LTI(Pega)	
 
300	Nagendla Manikanta
17PA1A04B0
Innoright Solutions	
 
301	Puppala Deepak Venkayya Naidu
17PA1A1248
Agiliq Info Solutions	
 
302	Payavula Ravi Kiran
19PA1E0045
Yupp TV	
 
303	Medapati Prasanna Kumar Reddy
17PA1A0371
Cognizant	
 
304	Mutyala Tarun Venkatesh
17PA1A05A4
MindTree	
 
305	Kukutla Meghana
17PA1A0581
MindTree	
 
306	Godavarthi Sri Sai Sruthi
17PA1A0543
MindTree	
 
307	Vegesna Bharathi
17PA1A1258
LTTS	
 
308	Kandula Tejaswini
17PA1A1220
LTTS	
 
309	Nammi Venkata Balamurali
17PA1A05A8
MindTree	
 
310	Vipparthi Vijaya Babu
18PA5A0519
LTTS	
 
311	Jalaparthi Rani
17PA1A1216
LTTS	
 
312	Aligina Sai Krishna
17PA1A0504
LTTS	
 
313	Akiri Bhanu Prakash
17PA1A0502
LTTS	
 
314	Telagareddy Nagendhar
18PA5A0433
LTTS	
 
315	Patcha Gowri Prathyusha Bhavani
17PA1A1245
LTTS	
 
316	Juveriya Tasneem
17PA1A1217
LTTS	
 
317	Mutyala Tarun Venkatesh
17PA1A05A4
LTTS	
 
318	Penumarthi Mounika
17PA1A05C7
Tech Mahindra(Pega)	
 
319	Kudipudi Yagna Sree Nagavalli
17PA1A1223
Tech Mahindra(Pega)	
 
320	Ayinampudi Samyuktha
17PA1A0508
Capgemini(Pega)	
 
321	Shaik Naseema
17PA1A04E6
Capgemini(Pega)	
 
322	Dunna Suresh
17PA1A0425
Capgemini(Pega)	
 
323	Kandukuri Rekha Sai Kumar
18PA5A0506
CTS(Pega)	
 
324	Vasukuri Naga Venkata Satish
18PA5A0434
CTS(Pega)	
 
325	Konapala Bala Siva Prasad
17PA1A0468
CTS(Pega)	
 
326	Karuturi Sai Jahnavi
17PA1A0459
CTS(Pega)	
 
327	Gadamsettti Venkata Ram Sai Praveen
17PA1A0426
CTS(Pega)	
 
328	Peddireddy Venkata Naga Santhosh
18PA5A0428
Areteans(Pega)	
 
329	Jaladani Venkateswararao
18PA5A0411
Areteans(Pega)	
 
330	Thota Govind Nikhil Durga Naga Kumar
17PA1A04F7
Areteans(Pega)	
 
331	Dirisala Lavanya
17PA1A0531
AMDOCS	
 
332	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
MindTree	
 
333	Varre Naga Venkata Suresh
17PA1A04G7
MindTree	
 
334	Vaddi Rohith
17PA1A04G3
MindTree	
 
335	Geddam Akhil
17PA1A0541
Virtusa	
 
336	Maddili Sunil Kumar
17PA1A0587
Global Logic	
 
337	R V S S Manibabu Ungarala
17PA1A04D6
Mindtree	
 
338	Vattiprolu Karthik
17PA1A04H0
Virtusa	
 
339	Nilla Leela Sai Balaji
17PA1A04B7
Capgemini	
 
340	Mohammed Nadeem
17PA1A0598
Capgemini	
 
341	Kolupuri Sai Venkata Sasank
17PA1A0573
Capgemini	
 
342	Vaddi Rohith
17PA1A04G3
Capgemini	
 
343	Challa Sateesh
17PA1A0419
Capgemini	
 
344	Nalla Venkata Sai Ram Mohan
17PA1A0266
Capgemini	
 
345	Mopidevi Jyothsna Devi
17PA1A1229
Capgemini	
 
346	Kudipudi Yagna Sree Nagavalli
17PA1A1223
Capgemini	
 
347	Ghanta Renuka Lakshmi
17PA1A1214
Capgemini	
 
348	Gogireddy Kavya
17PA1A0544
Capgemini	
 
349	Lankalapilli Sowmya
17PA1A0481
Capgemini	
 
350	Gaddam Sai Bhavana
17PA1A0427
Capgemini	
 
351	Metla D N V S S M Sri Harsha
17PA1A0496
Aaseya(Pega)	
 
352	Dhanani Sandeep
17PA1A0423
Aaseya(Pega)	
 
353	Neelapala Kusuma Sri
17PA1A1235
Aaseya(Pega)	
 
354	Satti Venkata Krishna Vamsi Reddy
17PA1A05E3
Aaseya(Pega)	
 
355	Penchikalapati Veera Bhupathi Dev
18PA5A0512
Capgemini	
 
356	Peddireddy Venkata Naga Santhosh
18PA5A0428
Capgemini	
 
357	Medapati Madhu Bala
18PA5A0422
Capgemini	
 
358	Kadulla Swathi
18PA5A0412
Capgemini	
 
359	Jaladani Venkateswararao
18PA5A0411
Capgemini	
 
360	Malladi Suresh Kumar
18PA5A0316
Capgemini	
 
361	Valavala Saiswetha
17PA1A1256
Capgemini	
 
362	Marripudi Anjani
17PA1A1226
Capgemini	
 
363	Kandikatla Aishwarya Robin
17PA1A1219
Capgemini	
 
364	Bellamkonda Rohin Surya Prakash
17PA1A1205
Capgemini	
 
365	Appada Aravinda Prakash
17PA1A1202
Capgemini	
 
366	Amujala Bhavana
17PA1A1201
Capgemini	
 
367	Vasamsetti Satyendra Prasad
17PA1A05G6
Capgemini	
 
368	Tumpudi Murali Sai Kamal Srikanth
17PA1A05G1
Capgemini	
 
369	Tenneti Likitha Sri Harshitha
17PA1A05F7
Capgemini	
 
370	Tammineedi Usha Naga Sri
17PA1A05F4
Capgemini	
 
371	Sayyed Hussain
17PA1A05E4
Capgemini	
 
372	Sadhanala Satya Sai Srivalli
17PA1A05D6
Capgemini	
 
373	Nunna Lakshmi Padmavathi
17PA1A05B7
Capgemini	
 
374	Nittala Lakshmi Sudeepthi
17PA1A05B5
Capgemini	
 
375	Neduri Veera Venkata Ram Pandu
17PA1A05B1
Capgemini	
 
376	Medepalli Chandana
17PA1A0594
Capgemini	
 
377	Manne Tejaswini Sri Naga Sai
17PA1A0592
Capgemini	
 
378	Kusumanchi Lakshmi Mani Deepika
17PA1A0583
Capgemini	
 
379	Koppuravuri Dakshayani Manozna
17PA1A0578
Capgemini	
 
380	Kone Srimannarayana
17PA1A0577
Capgemini	
 
381	Kayala Sai Vamsi
17PA1A0570
Capgemini	
 
382	Kallepalli Shalini
17PA1A0564
Capgemini	
 
383	Kadiyala Hemanth Sai Srinivas
17PA1A0561
Capgemini	
 
384	Kaddala Siva Kumar
17PA1A0560
Capgemini	
 
385	Jillella Meghana Priya
17PA1A0558
Capgemini	
 
386	Jampana Sri Guru Vyshnavi
17PA1A0557
Capgemini	
 
387	Irrinki Neelima Devi
17PA1A0554
Capgemini	
 
388	Induri Bhaskaranagavenkatesh
17PA1A0553
Capgemini	
 
389	Grandhi Sri Ram
17PA1A0549
Capgemini	
 
390	Gopisetti Lahari
17PA1A0545
Capgemini	
 
391	Garapati Bulli Ramesh
17PA1A0539
Capgemini	
 
392	Garaga Yathish Bhargav
17PA1A0538
Capgemini	
 
393	Eada Kamal Tej Reddy
17PA1A0532
Capgemini	
 
394	Dalu Thanmay
17PA1A0526
Capgemini	
 
395	Choragudi Sai Praveen
17PA1A0524
Capgemini	
 
396	Chinni Alekhya
17PA1A0522
Capgemini	
 
397	Bandi Likhitha Ramalakshmi
17PA1A0511
Capgemini	
 
398	Yelubandi Naga Manohar
17PA1A04H7
Capgemini	
 
399	Vungarala Ranjith Sai Venkat
17PA1A04H5
Capgemini	
 
400	Veerni Sai Venkata Durga Asish
17PA1A04H1
Capgemini	
 
401	Varre Naga Venkata Suresh
17PA1A04G7
Capgemini	
 
402	Valluripalli Varunsai
17PA1A04G6
Capgemini	
 
403	Tulasi Ravi Kiran
17PA1A04G1
Capgemini	
 
404	Thota Govind Nikhil Durga Naga Kumar
17PA1A04F7
Capgemini	
 
405	Tamarapalli Naga Vamsi Santhosh
17PA1A04F4
Capgemini	
 
406	Sai Madhuri Kappaganthula
17PA1A04E1
Capgemini	
 
407	Poshala Praneeth Goud
17PA1A04D3
Capgemini	
 
408	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
Capgemini	
 
409	Pasumarthi Harsha Vardhan
17PA1A04C4
Capgemini	
 
410	Palleti Krupa Sravanthi
17PA1A04B9
Capgemini	
 
411	Pala Sri Padma Paanidhar
17PA1A04B8
Capgemini	
 
412	Nidamanuri Venkata Sai Kumar
17PA1A04B6
Capgemini	
 
413	Nelluri Yamini Lakshmi Tirupathamma
17PA1A04B5
Capgemini	
 
414	Mullapudi Sai Prapoorna
17PA1A04A5
Capgemini	
 
415	Mopidevi Purna
17PA1A0499
Capgemini	
 
416	Mekala Mohanvenkat Sai
17PA1A0494
Capgemini	
 
417	Mandavilli Rama Yavanika
17PA1A0490
Capgemini	
 
418	Garapati Lakshmi Veera Venkata Sairamkumar
17PA1A0430
Capgemini	
 
419	Dammuluri Yogendra Sai Teja
17PA1A0421
Capgemini	
 
420	Chakka Neha
17PA1A0418
Capgemini	
 
421	Ampa Revathi
17PA1A0405
Capgemini	
 
422	Sarikonda Venkata Nishanth Kumar Raju
17PA1A03A4
Capgemini	
 
423	Mattaparthi Venkata Ramana
17PA1A0370
Capgemini	
 
424	Malakala Sai Venkatesh
17PA1A0365
Capgemini	
 
425	Kantimahanthi Bhargav Sudhakar Patnaik
17PA1A0350
Capgemini	
 
426	Gubbala Vivek
17PA1A0331
Capgemini	
 
427	Datla Lakshmi Sai Aparna
17PA1A0323
Capgemini	
 
428	Chodagiri Sandeep
17PA1A0320
Capgemini	
 
429	Anisetti Teja Mani Raja
17PA1A0304
Capgemini	
 
430	Yalla Jnaneswari Sri Rama Manimala
17PA1A02B2
Capgemini	
 
431	Vytla Sri Varsha
17PA1A02B0
Capgemini	
 
432	Tota Anil Babu
17PA1A0299
Capgemini	
 
433	Sunkara Chandu Kumar
17PA1A0291
Capgemini	
 
434	Satyavolu Venkat Sai Charan
17PA1A0288
Capgemini	
 
435	Pindi Naga Satya Sai Rajesh
17PA1A0275
Capgemini	
 
436	Nulu Jagadeesh Gupta
17PA1A0267
Capgemini	
 
437	Mekala Kavya Naga Sri Sai
17PA1A0257
Capgemini	
 
438	Korla Sri Himaja Sitadevi
17PA1A0249
Capgemini	
 
439	Devarapu Vishnu Sai Sri Nataraj
17PA1A0223
Capgemini	
 
440	Addanki Soumya
17PA1A0202
Capgemini	
 
441	Shaik Pavan Kumar
17PA1A0152
Capgemini	
 
442	Unikela Sowmya
17PA1A02A1
Capgemini	
 
443	Polumati Vamsidhar
17PA1A0395
Capgemini	
 
444	Muppidi Pranam
17PA1A05A3
Capgemini	
 
445	Ponna Narendra
17PA1A0396
Capgemini	
 
446	Dendukuri Venkata Ramaraju
18PA5A0307
Capgemini	
 
447	Chavali Sai Achyuta Prakash
17PA1A0109
Capgemini	
 
448	Buri Tejaswi
17PA1A1207
Capgemini	
 
449	Upputuri Bhanu Kalyan
17PA1A1255
Capgemini	
 
450	Deepti Srimai Bolloju
17PA1A0222
Capgemini	
 
451	Valluri Jaswanth
17PA1A02A5
Capgemini	
 
452	Velpuri P N V Venkata Satya Chaithanya
17PA1A02A7
Capgemini	
 
453	Kanakala Yeswanth
17PA1A0345
Capgemini	
 
454	Mygapula Sai Praveen
17PA1A0379
Capgemini	
 
455	Akurathi Mounika Sai
17PA1A0503
Capgemini	
 
456	Mukku Nandini
17PA1A04A3
Capgemini	
 
457	Naveen Kumar Tummidi
17PA1A04B3
Capgemini	
 
458	Nethala Naveen
17PA1A0383
Capgemini	
 
459	Bonthu Lavanya
17PA1A0515
TA Digital	
 
460	Palla Kesava
18PA5A0425
Coforge	
 
461	Pamoti Vasudeva Manikanta
18PA5A0220
Coforge	
 
462	Kothapalli Hanumansatyasuryamanikanta
18PA5A0217
Coforge	
 
463	Chintoju Ram Prasanth
18PA5A0208
Coforge	
 
464	Bonthu Lavanya
17PA1A0515
Coforge	
 
465	Anusri Satya Sri
18PA5A0205
Coforge	
 
466	Rudraraju Hemanthi Malavika
17PA1A04D9
Coforge	
 
467	Nadendla Bhanu Sri
17PA1A04A9
Coforge	
 
468	Malepati Mallikarjuna
17PA1A0486
Coforge	
 
469	Lalam Latha Sri
17PA1A0478
Coforge	
 
470	Gudimetla Datta Bheema Teja
17PA1A0333
Coforge	
 
471	Gubbala Trinadh Sankeerth
17PA1A0330
Coforge	
 
472	Dalli Rohit Ganesh
17PA1A0321
Coforge	
 
473	Malluru Harshitha
17PA1A0590
Broadridge	
 
474	Nabigaru Dileep Kumar
17PA1A05A5
Broadridge	
 
475	Manda Sai Sri
17PA1A0488
TCS NQT - Ninja	
 
476	Goteti Venkatesh
17PA1A0432
TCS NQT - Ninja	
 
477	Samudrala Vishnu Vardhan
18PA5A0516
TCS NQT - Ninja	
 
478	Guttula Jaya Balaji
18PA5A0213
TCS NQT - Ninja	
 
479	Mandela Shiva
18PA5A0229
TCS NQT - Ninja	
 
480	Sambrani Chandana Mani Deepika
17PA1A0283
TCS NQT - Ninja	
 
481	Sheik Sharuk
17PA1A05F0
TCS NQT - Ninja	
 
482	Vulluri Sobha Sudeepthi
17PA1A04H4
TCS NQT - Ninja	
 
483	Peddiboyina Rajesh
18PA5A0427
TCS NQT - Ninja	
 
484	Uggam Venkatadri
18PA5A0225
TCS NQT - Ninja	
 
485	Koncha Abhinava Madhu Kishore
17PA1A0355
TCS NQT - Ninja	
 
486	Macha Durga Prasad
17PA1A0363
TCS NQT - Ninja	
 
487	Kommu Rahul
17PA1A0354
TCS NQT - Ninja	
 
488	Darabattula Sandeep
18PA5A0209
TCS NQT - Ninja	
 
489	Perumalla Sai Praveen
17PA1A0390
TCS NQT - Ninja	
 
490	Chiluvuri Satya Surendra Raju
17PA1A0316
TCS NQT - Ninja	
 
491	Nachu N D V Prasad
17PA1A1231
TCS NQT - Ninja	
 
492	Veeravalli Vijaya Lakshmi
18PA5A0435
TCS NQT - Ninja	
 
493	Pithani Satya Sai Kiran
18PA5A0431
TCS NQT - Ninja	
 
494	Kollu Nithin Varma
18PA5A0315
TCS NQT - Ninja	
 
495	Ganta Naga Durga Rao
18PA5A0308
TCS NQT - Ninja	
 
496	Vaddimukkala Rahul
18PA5A0227
TCS NQT - Ninja	
 
497	Chennuri Prasanth Kumar
18PA5A0304
TCS NQT - Ninja	
 
498	Kanuri Rama Venkata Siva Sai
18PA5A0214
TCS NQT - Ninja	
 
499	Varre Naga Venkata Suresh
17PA1A04G7
TCS NQT - Ninja	
 
500	Anusri Satya Sri
18PA5A0205
TCS NQT - Ninja	
 
501	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
TCS NQT - Ninja	
 
502	Nadendla Bhanu Sri
17PA1A04A9
TCS NQT - Ninja	
 
503	Gubbala Trinadh Sankeerth
17PA1A0330
TCS NQT - Ninja	
 
504	Mangina Venkata Kiran
17PA1A0366
TCS NQT - Ninja	
 
505	Chodagiri Sandeep
17PA1A0320
TCS NQT - Ninja	
 
506	Bellamkonda Baba Badrinath
17PA1A0309
TCS NQT - Ninja	
 
507	Yarra Lakshmana Rao
17PA1A02B3
TCS NQT - Ninja	
 
508	Purigalla Sravani
17PA1A0278
TCS NQT - Ninja	
 
509	Syed Kareem Siraz
17PA1A0294
TCS NQT - Ninja	
 
510	Pedapati Balaram Sandeep
17PA1A0272
TCS NQT - Ninja	
 
511	Korla Sri Himaja Sitadevi
17PA1A0249
TCS NQT - Ninja	
 
512	Bathula Kesava Hemanth
17PA1A0208
TCS NQT - Ninja	
 
513	Giddha Dhanagni Posi Babu
17PA1A0227
TCS NQT - Ninja	
 
514	Veeranki Khyathi Sri
17PA1A0157
TCS NQT - Ninja	
 
515	Akurathi Nikhil
17PA1A0203
TCS NQT - Ninja	
 
516	Nakkani Naga Devi Apparao
17PA1A0264
NTT Data	
 
517	Angara Hari Teja
18PA5A0204
TCS NQT - Ninja	
 
518	Metla D N V S S M Sri Harsha
17PA1A0496
TCS NQT - Ninja	
 
519	Alpati Pravin Vasu
17PA1A0302
TCS NQT - Ninja	
 
520	Kosuru Gopi
17PA1A0357
TCS NQT - Ninja	
 
521	Satyavolu Venkat Sai Charan
17PA1A0288
TCS NQT - Ninja	
 
522	Malineni Dileep
17PA1A0253
TCS NQT - Ninja	
 
523	Sagi Sai Gopala Raju
17PA1A04E0
TCS NQT - Ninja	
 
524	Muthyala T V Kishore Babu
17PA1A04A7
TCS NQT - Ninja	
 
525	Konapala Bala Siva Prasad
17PA1A0468
TCS NQT - Ninja	
 
526	Pilla Haridev
17PA1A0391
TCS NQT - Ninja	
 
527	Penumalla Venkatesh
17PA1A0388
TCS NQT - Ninja	
 
528	Vabilisetty H S R S Venkatesh
17PA1A02A4
TCS NQT - Ninja	
 
529	Mangina Rajesh
18PA5A0317
TCS NQT - Ninja	
 
530	Sri Krishna Chaitanya Varma D
18PA5A0224
TCS NQT - Ninja	
 
531	Madepalli V V D G Sivanagu
18PA5A0218
TCS NQT - Ninja	
 
532	Valavala Saiswetha
17PA1A1256
TCS NQT - Ninja	
 
533	Penmetsa Shanmitha Pooja
17PA1A1246
TCS NQT - Ninja	
 
534	Appada Aravinda Prakash
17PA1A1202
TCS NQT - Ninja	
 
535	Vasamsetti Satyendra Prasad
17PA1A05G6
TCS NQT - Ninja	
 
536	Vasa Purna Nagendra Prasad
17PA1A05G5
TCS NQT - Ninja	
 
537	Sunkara Pavan Kalyan Ayyappa
17PA1A05F1
TCS NQT - Ninja	
 
538	Sala Vijay Kumar
17PA1A05D9
TCS NQT - Ninja	
 
539	Sandrana Madhava Sai
17PA1A05E1
TCS NQT - Ninja	
 
540	Rebba Achyuta Ram
17PA1A05D5
TCS NQT - Ninja	
 
541	Parikela Moni Adithya
17PA1A05C4
TCS NQT - Ninja	
 
542	Nunna Lakshmi Padmavathi
17PA1A05B7
TCS NQT - Ninja	
 
543	Nammi Venkata Balamurali
17PA1A05A8
TCS NQT - Ninja	
 
544	Kukutla Meghana
17PA1A0581
TCS NQT - Ninja	
 
545	Karri Surya Teja
17PA1A0568
TCS NQT - Ninja	
 
546	Gopisetti Lahari
17PA1A0545
TCS NQT - Ninja	
 
547	Chinni Alekhya
17PA1A0522
TCS NQT - Ninja	
 
548	Kalidindi Pooja Sahithi
17PA1A0451
TCS NQT - Ninja	
 
549	Yetukuri Sandeepvarma
17PA1A02B5
TCS NQT - Ninja	
 
550	Chirapa Purna Venkata Satya Sai Trinadh
17PA1A0319
TCS NQT - Ninja	
 
551	Yalla Jnaneswari Sri Rama Manimala
17PA1A02B2
TCS NQT - Ninja	
 
552	Dharkshan Pavankumar
17PA1A0224
TCS NQT - Ninja	
 
553	Sadhanala Satya Sai Srivalli
17PA1A05D6
Infosys SE(Through HackWithinfy)	
 
554	Penchikalapati Veera Bhupathi Dev
18PA5A0512
TCS Pega	
 
555	Kadulla Swathi
18PA5A0412
TCS Pega	
 
556	Mattaparthi Bharath Kumar
18PA5A0421
TCS Pega	
 
557	Gangineni Prathyusha
18PA5A0408
TCS Pega	
 
558	Gadamsetty Mohith
18PA5A0407
TCS Pega	
 
559	Nalla Kishore
17PA1A1232
TCS Pega	
 
560	Veeramachaneni Rashmitha
17PA1A1257
TCS Pega	
 
561	Atava Ayyappa Swamy
17PA1A1203
TCS Pega	
 
562	Amujala Bhavana
17PA1A1201
TCS Pega	
 
563	Dirisena Mercy Hepsiba
17PA1A05H5
TCS Pega	
 
564	Yalamati Rohini
17PA1A05H1
TCS Pega	
 
565	Yarlagadda Namratha
17PA1A05H2
TCS Pega	
 
566	Yadlapalli P G Narasimha Rao
17PA1A05H0
TCS Pega	
 
567	Syed Sajeeda Begum
17PA1A05F3
TCS Pega	
 
568	Vanapalli Lakshmi Srujan
17PA1A05G2
TCS Pega	
 
569	Seelamsetti V N Sindhu Sha
17PA1A05E5
TCS Pega	
 
570	Swarna Sai Prasanka
17PA1A05F2
TCS Pega	
 
571	Sarede Jagadhiswari
17PA1A05E2
TCS Pega	
 
572	Ponnaganti Vasantha Lakshmi
17PA1A05D0
TCS Pega	
 
573	Pallantla Devendrakumar
17PA1A05C2
TCS Pega	
 
574	Mallela Praveen
17PA1A0588
TCS Pega	
 
575	Medepalli Chandana
17PA1A0594
TCS Pega	
 
576	Likhithapudi Noel
17PA1A0584
TCS Pega	
 
577	Gurram Anand Paul
17PA1A0551
TCS Pega	
 
578	Goriparthi Anvitha
17PA1A0547
TCS Pega	
 
579	Dalu Thanmay
17PA1A0526
TCS Pega	
 
580	Dasari Meghana
17PA1A0529
TCS Pega	
 
581	Bandi Likhitha Ramalakshmi
17PA1A0511
TCS Pega	
 
582	Annepu Sahasra
17PA1A0507
TCS Pega	
 
583	Alluri Vishnu Vardhan Varma
17PA1A0505
TCS Pega	
 
584	Vulluri Sobha Sudeepthi
17PA1A04H4
TCS Pega	
 
585	Vegi Bhanu Adinarayana
17PA1A04H2
TCS Pega	
 
586	Ummadi Satya Jai Deep
17PA1A04G2
TCS Pega	
 
587	Thota Tulasi Chinna Gopala Swamy
17PA1A04F8
TCS Pega	
 
588	Somisetty Chandra Mouli
17PA1A04F0
TCS Pega	
 
589	Tamarapalli Naga Vamsi Santhosh
17PA1A04F4
TCS Pega	
 
590	Sai Madhuri Kappaganthula
17PA1A04E1
TCS Pega	
 
591	Shaik Asha
17PA1A04E5
TCS Pega	
 
592	Rayudu Anand Santhi Kiran
17PA1A04D8
TCS Pega	
 
593	Poshala Praneeth Goud
17PA1A04D3
TCS Pega	
 
594	Nelivada Santoshi
17PA1A04B4
TCS Pega	
 
595	Penmetsa Satish Varma
17PA1A04C9
TCS Pega	
 
596	Narra Manohar
17PA1A04B2
TCS Pega	
 
597	Miriyala Vihari
17PA1A0497
TCS Pega	
 
598	Mullapudi Sai Prapoorna
17PA1A04A5
TCS Pega	
 
599	Madana Venkata Nagasai Phanipavan
17PA1A0482
TCS Pega	
 
600	Mekala Mohanvenkat Sai
17PA1A0494
TCS Pega	
 
601	Komatlapalli Sai Teja
17PA1A0464
TCS Pega	
 
602	Kotikalapudi Phaneendra
17PA1A0475
TCS Pega	
 
603	Kavuru Hema Latha
17PA1A0460
TCS Pega	
 
604	Kamuju Navya Supriya
17PA1A0455
TCS Pega	
 
605	Indukuri Siva Sai Vijaya Ramaraju
17PA1A0440
TCS Pega	
 
606	Gandikota Bhargava Sai
17PA1A0428
TCS Pega	
 
607	Devarapu Jaya Chand
17PA1A0422
TCS Pega	
 
608	Chollangi Sai Pavan
17PA1A0420
TCS Pega	
 
609	Bhupathiraju Sri Sai Pavan Varma
17PA1A0413
TCS Pega	
 
610	Bonam Kiran Teja
17PA1A0416
TCS Pega	
 
611	Bachu Eswar
17PA1A0408
TCS Pega	
 
612	Balagam Udaya Sriteja
17PA1A0409
TCS Pega	
 
613	Annamneedi Venkata Srinivas
17PA1A0407
TCS Pega	
 
614	Ampa Revathi
17PA1A0405
TCS Pega	
 
615	Dasari Suneeta
18PA5A0505
Infosys (Through InfyTQ)	
 
616	Ande Revathi Lakshmi Sravani
18PA5A0501
Infosys (Through InfyTQ)	
 
617	Relangi Sai Naga Venkata Harsha Vardhan
17PA1A1249
Infosys (Through InfyTQ)	
 
618	Nekkalapudi Rama Lakshmi
17PA1A1237
Infosys (Through InfyTQ)	
 
619	Nekkalapudi Basanth
17PA1A1236
Infosys (Through InfyTQ)	
 
620	Nangineedi Naresh Babu
17PA1A1234
Infosys (Through InfyTQ)	
 
621	Bellamkonda Rohin Surya Prakash
17PA1A1205
Infosys (Through InfyTQ)	
 
622	Vasamsetti Satyendra Prasad
17PA1A05G6
Infosys (Through InfyTQ)	
 
623	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
Infosys (Through InfyTQ)	
 
624	Tenneti Likitha Sri Harshitha
17PA1A05F7
Infosys (Through InfyTQ)	
 
625	Tenali Priya Chandana
17PA1A05F6
Infosys (Through InfyTQ)	
 
626	Tammineedi Usha Naga Sri
17PA1A05F4
Infosys (Through InfyTQ)	
 
627	Sadhanala Satya Sai Srivalli
17PA1A05D6
Infosys (Through InfyTQ)	
 
628	Padarthi Rangarao
17PA1A05B9
Infosys (Through InfyTQ)	
 
629	Nunna Lakshmi Padmavathi
17PA1A05B7
Infosys (Through InfyTQ)	
 
630	Nittala Lakshmi Sudeepthi
17PA1A05B5
Infosys (Through InfyTQ)	
 
631	Narina Tharaka Sai Ram
17PA1A05B0
Infosys (Through InfyTQ)	
 
632	Manne Tejaswini Sri Naga Sai
17PA1A0592
Infosys (Through InfyTQ)	
 
633	Kothagundu Venkata Krishna Rao
17PA1A0579
Infosys (Through InfyTQ)	
 
634	Koppuravuri Dakshayani Manozna
17PA1A0578
Infosys (Through InfyTQ)	
 
635	Kone Srimannarayana
17PA1A0577
Infosys (Through InfyTQ)	
 
636	Kolla Ravi Teja
17PA1A0571
Infosys (Through InfyTQ)	
 
637	Kayala Sai Vamsi
17PA1A0570
Infosys (Through InfyTQ)	
 
638	Katta Monika
17PA1A0569
Infosys (Through InfyTQ)	
 
639	Karri Surya Teja
17PA1A0568
Infosys (Through InfyTQ)	
 
640	Jampana Sri Guru Vyshnavi
17PA1A0557
Infosys (Through InfyTQ)	
 
641	Garapati Bulli Ramesh
17PA1A0539
Infosys (Through InfyTQ)	
 
642	Garaga Yathish Bhargav
17PA1A0538
Infosys (Through InfyTQ)	
 
643	Eada Kamal Tej Reddy
17PA1A0532
Infosys (Through InfyTQ)	
 
644	Chinni Alekhya
17PA1A0522
Infosys (Through InfyTQ)	
 
645	Veerni Sai Venkata Durga Asish
17PA1A04H1
Infosys (Through InfyTQ)	
 
646	Vaddi Rohith
17PA1A04G3
Infosys (Through InfyTQ)	
 
647	Sunkavilli Suranya
17PA1A04F2
Infosys (Through InfyTQ)	
 
648	Polisetti Satya Siva Cahndra Hasa
17PA1A04D2
Infosys (Through InfyTQ)	
 
649	Muthyala T V Kishore Babu
17PA1A04A7
Infosys (Through InfyTQ)	
 
650	Manam Narayana Rao
17PA1A0487
Infosys (Through InfyTQ)	
 
651	Magapu Jahnavi Devi
17PA1A0485
Infosys (Through InfyTQ)	
 
652	Madeti Pavani N S S M K Priyanka
17PA1A0484
Infosys (Through InfyTQ)	
 
653	Koppula Jyothi Satya Lakshmi Sai Ajay
17PA1A0471
Infosys (Through InfyTQ)	
 
654	Kokkirala Dinesh Venkata Sai
17PA1A0462
Infosys (Through InfyTQ)	
 
655	Kanteti Janardhana Gupta
17PA1A0457
Infosys (Through InfyTQ)	
 
656	Kamisetti Som Sekhar
17PA1A0454
Infosys (Through InfyTQ)	
 
657	Jeji Srinivasa Vinnakota
17PA1A0446
Infosys (Through InfyTQ)	
 
658	Garapati Lakshmi Veera Venkata Sairamkumar
17PA1A0430
Infosys (Through InfyTQ)	
 
659	Dammuluri Yogendra Sai Teja
17PA1A0421
Infosys (Through InfyTQ)	
 
660	Adabala Mahesh Babu
17PA1A0402
Infosys (Through InfyTQ)	
 
661	Addanki Soumya
17PA1A0202
Infosys (Through InfyTQ)	
 
662	Abburi Pavani
17PA1A0201
Infosys (Through InfyTQ)	
 
663	Chakka Vishnu Satya Raghu Vamsi
17PA1A0518
TCS NQT - Ninja	
 
664	Sheik Sharuk
17PA1A05F0
TCS NQT - Ninja	
 
665	Akurathi Raja Sekhar
18PA5A0402
TCS NQT - Ninja	
 
666	Goda Ramakrishna
17PA1A0431
HCL	
 
667	Bhupathiraju Indhu Priya
17PA1A0209
TCS NQT - Ninja	
 
668	Unikela Sowmya
17PA1A02A1
DXC	
 
669	Mekala Kavya Naga Sri Sai
17PA1A0257
TCS NQT - Ninja	
 
670	Chavali Sai Achyuta Prakash
17PA1A0109
TCS NQT - Ninja	
 
671	Bokka Sumanth
17PA1A0415
TCS NQT - Ninja	
 
672	Bokka Rahul
17PA1A0211
TCS NQT - Ninja	
 
673	Chinnamsetty Anilkumar
17PA1A0218
TCS NQT - Ninja	
 
674	Chinta Uma Nagendra Varma
17PA1A0219
TCS NQT - Ninja	
 
675	Kommana Prasanna Kumar
17PA1A0248
TCS NQT - Ninja	
 
676	Mandapaka Paramesh
17PA1A0256
TCS NQT - Ninja	
 
677	Ogirala Sowjanya
17PA1A0268
TCS NQT - Ninja	
 
678	Seelaboina Lavanya
17PA1A0289
DXC	
 
679	Valluri Jaswanth
17PA1A02A5
TCS NQT - Ninja	
 
680	Dasari Ravi Chandra
18PA5A0210
TCS NQT - Ninja	
 
681	Doddavarapu Subrahmanyam
18PA5A0211
HCL	
 
682	Bokka Tejaswi Satya Pavan
17PA1A0212
TCS NQT - Ninja	
 
683	Grandi Vijay Kumar
17PA1A0231
TCS NQT - Ninja	
 
684	Kema Hemanth Kumar
17PA1A0243
TCS NQT - Ninja	
 
685	Bathula Bhavani Harihara Kumar
17PA1A0308
TCS NQT - Ninja	
 
686	Jalla Vijay Kumar Raju
17PA1A0338
TCS NQT - Ninja	
 
687	Kampati Nitish Venkata Satya Sai Teja
17PA1A0344
TCS NQT - Ninja	
 
688	Kanchumarthi Rithwik Venkatesh
17PA1A0346
TCS NQT - Ninja	
 
689	Koppisetti Satya Prasad
17PA1A0356
TCS NQT - Ninja	
 
690	Kudapa Balaram Chowdary
17PA1A0358
TCS NQT - Ninja	
 
691	Kukkala Pavan Kumar
17PA1A0359
TCS NQT - Ninja	
 
692	Maraka Rohit Kumar
17PA1A0368
TCS NQT - Ninja	
 
693	Melam Chatresh Narayan
17PA1A0374
Infosys	
 
694	Muppala Sai Nayan
17PA1A0377
TCS NQT - Ninja	
 
695	Nirjogi Balaji Sai Prakash
17PA1A0384
TCS NQT - Ninja	
 
696	Padala Sai Krishna
17PA1A0385
TCS NQT - Ninja	
 
697	Pericherla Siva Naga Raju
17PA1A0389
TCS NQT - Ninja	
 
698	Pithani Jaya Pradeep
17PA1A0392
TCS NQT - Ninja	
 
699	Pusapati Hemanth Upendra Reddy
17PA1A0398
TCS NQT - Ninja	
 
700	Raavi Mallikarjuna
17PA1A0399
TCS NQT - Ninja	
 
701	Venuganti Subhash Chandra Bose
17PA1A03B5
TCS NQT - Ninja	
 
702	Nemani Ganesh
17PA1A05B3
TCS NQT - Ninja	
 
703	Veerapogu Praveen
17PA1A05G7
TCS NQT - Ninja	
 
704	Jogi Narendra
18PA5A0313
TCS NQT - Ninja	
 
705	Vanapalli Tirumala Vasu
18PA5A0326
TCS NQT - Ninja	
 
706	Vajjiparthi Yaswanth Krishna
18PA5A0328
TCS NQT - Ninja	
 
707	Chinni Chaithanya
17PA1A0317
DXC	
 
708	Gangisetti Sai Satish Kumar
18PA1A0438
TCS NQT - Ninja	
 
709	Bokka Krishna Prasad
18PA5A0403
TCS NQT - Ninja	
 
710	Lingineni Bindu Prasanna Lakshmi
18PA5A0416
TCS NQT - Ninja	
 
711	Odugu Venkatraju
18PA5A0424
TCS NQT - Ninja	
 
712	Kovvuri Harsha Sai Saroja Reddy
17PA1A0128
TCS NQT - Ninja	
 
713	Malepati Mallikarjuna
17PA1A0486
Wipro	
 
714	Vanamatla Pavan Kumar
17PA1A03B1
Infosys	
 
715	Kandikatla Aishwarya Robin
17PA1A1219
TATA Elxsi	
 
716	Kothari Balu Phanendra
18PA5A0508
Wipro	
 
717	Tirumala Sai Sandeep
18PA5A0231
Wipro	
 
718	G Monisha
17PA1A0535
Wipro	
 
719	Shaik Ashwah
17PA1A05E7
Wipro	
 
720	Badeti Pardha Saradhi
18PA5A0502
Wipro	
 
721	Yamalavalasa Supriya
18PA5A0437
Wipro	
 
722	Saride Durga Prasanna
18PA5A0223
Wipro	
 
723	Ainam Sai Manikantha
18PA5A0201
Wipro	
 
724	Vegesna Bharathi
17PA1A1258
Wipro	
 
725	Nowkatla Harshavardhini
17PA1A1242
Wipro	
 
726	Didla Vijay Stalin Babu
17PA1A0530
Wipro	
 
727	Thonta Lakshmi Sai Teja
17PA1A04F6
Wipro	
 
728	Muthyala T V Kishore Babu
17PA1A04A7
Wipro	
 
729	Metla D N V S S M Sri Harsha
17PA1A0496
Wipro	
 
730	Madeti Pavani N S S M K Priyanka
17PA1A0484
Wipro	
 
731	Grandhi Venkatesh
17PA1A0434
Wipro	
 
732	Tota Anil Babu
17PA1A0299
Wipro	
 
733	Seelam Vinay Kumar Reddy
17PA1A0290
Wipro	
 
734	Nakkani Naga Devi Apparao
17PA1A0264
Wipro	
 
735	Kalla Sreeram
17PA1A0239
Wipro	
 
736	Piridi Someswara Sai Kumar
17PA1A04D0
Hexaware	
 
737	Mulagapati Sasank Siddhardha
18PA5A0510
Verzeo Edutech Pvt Ltd	
 
738	Challa Sateesh
17PA1A0419
Hexaware	
 
739	Kandula Tejaswini
17PA1A1220
Wipro	
 
740	Bellamkonda Rohin Surya Prakash
17PA1A1205
Wipro	
 
741	Shaik Vali
17PA1A05E9
Wipro	
 
742	Samudrala Vishnu Vardhan
18PA5A0516
Wipro	
 
743	Marisetti Dunti Ganesh
18PA5A0509
Wipro	
 
744	Kanuri Rama Venkata Siva Sai
18PA5A0214
Wipro	
 
745	Nangineedi Naresh Babu
17PA1A1234
Wipro	
 
746	Kudupudi Rajesh Kumar
17PA1A1224
Wipro	
 
747	Munukoti Sai Sri Hari Chandana
17PA1A1230
Wipro	
 
748	Padarthi Rangarao
17PA1A05B9
Wipro	
 
749	Vanapalli Sridevi
17PA1A05G3
Wipro	
 
750	Grandhi Himavarshini
17PA1A0548
Wipro	
 
751	Bezawada Sadhvi
17PA1A0512
Wipro	
 
752	Piridi Someswara Sai Kumar
17PA1A04D0
Wipro	
 
753	Pasumarthi Harsha Vardhan
17PA1A04C4
Wipro	
 
754	Pala Sri Padma Paanidhar
17PA1A04B8
Wipro	
 
755	Kotikalapudi Phaneendra
17PA1A0475
Wipro	
 
756	Jampana Sai Deepika
17PA1A0445
Wipro	
 
757	Kokkirala Dinesh Venkata Sai
17PA1A0462
Wipro	
 
758	Yalla Jnaneswari Sri Rama Manimala
17PA1A02B2
Wipro	
 
759	Ogirala Sowjanya
17PA1A0268
Wipro	
 
760	Purigalla Sravani
17PA1A0278
Wipro	
 
761	Muppana Siva Sai Kumar
17PA1A0263
Wipro	
 
762	Mudunuri Meher Krishna Varma
17PA1A0261
Wipro	
 
763	Akurathi Nikhil
17PA1A0203
Wipro	
 
764	Marisetti Dunti Ganesh
18PA5A0509
Infosys	
 
765	Kanchipogu Vamsi
18PA5A0314
Infosys	
 
766	Marada Mouli Santosh Sai
18PA5A0318
Infosys	
 
767	Tirumala Sai Sandeep
18PA5A0231
Infosys	
 
768	Pamoti Vasudeva Manikanta
18PA5A0220
Infosys	
 
769	Mandela Shiva
18PA5A0229
Infosys	
 
770	Pakalapati Sai Vijay
18PA5A0108
Infosys	
 
771	Ainam Sai Manikantha
18PA5A0201
Infosys	
 
772	Munukoti Sai Sri Hari Chandana
17PA1A1230
Infosys	
 
773	Lokam Jhnana Reshmika
17PA1A1225
Infosys	
 
774	Thiparthi Sai Sandeep
17PA1A05F8
Infosys	
 
775	Shaik Vali
17PA1A05E9
Infosys	
 
776	Penumarthi Mounika
17PA1A05C7
Infosys	
 
777	Gorantla Raga Swarupa
17PA1A0546
Infosys	
 
778	Chakka Vishnu Satya Raghu Vamsi
17PA1A0518
Infosys	
 
779	Gogireddy Kavya
17PA1A0544
Infosys	
 
780	Isukapati Chakravarthy
17PA1A0442
Infosys	
 
781	Jagarlamudi Mohana Naresh
17PA1A0443
Infosys	
 
782	Perumalla Sai Praveen
17PA1A0390
Infosys	
 
783	Vanga Sai Kondala Satwik
17PA1A03B2
Infosys	
 
784	Medapati Vamsi
17PA1A0372
Infosys	
 
785	Navadu Leela Venkata Gowtham Krishna
17PA1A0382
Infosys	
 
786	Gubbala Trinadh Sankeerth
17PA1A0330
Infosys	
 
787	Balina Mentraju
17PA1A0306
Infosys	
 
788	Yarra Lakshmana Rao
17PA1A02B3
Infosys	
 
789	Sambrani Chandana Mani Deepika
17PA1A0283
Infosys	
 
790	Seelam Vinay Kumar Reddy
17PA1A0290
Infosys	
 
791	Nakkani Naga Devi Apparao
17PA1A0264
Infosys	
 
792	Konala Naveen Satya Sankar Reddy
17PA1A0126
Infosys	
 
793	Padarthi Rangarao
17PA1A05B9
Hexaware	
 
794	Tammineedi Usha Naga Sri
17PA1A05F4
Wipro	
 
795	Gannamani Siva Sankar
17PA1A0537
Wipro	
 
796	Koppula Jyothi Satya Lakshmi Sai Ajay
17PA1A0471
Wipro	
 
797	Shaik Ashwah
17PA1A05E7
Global edge	
 
798	Juveriya Tasneem
17PA1A1217
Global edge	
 
799	Kudupudi Rajesh Kumar
17PA1A1224
Acel Solutions	
 
800	Gubbala Venkata Satya
17PA1A0435
Evoke(Pega)	
 
801	Daivapu Satya Teja
18PA5A0305
Rane	
 
802	Vighnesh Guttula
17PA1A03B6
Rane	
 
803	Patcha Gowri Prathyusha Bhavani
17PA1A1245
CGI	
 
804	Munukoti Sai Sri Hari Chandana
17PA1A1230
CGI	
 
805	Matlapudi N V Manasa
17PA1A1227
CGI	
 
806	Gogireddy Kavya
17PA1A0544
CGI	
 
807	Godavarthi Sri Sai Sruthi
17PA1A0543
CGI	
 
808	Bonthu Lavanya
17PA1A0515
CGI	
 
809	Shaik Naseema
17PA1A04E6
CGI	
 
810	Korivi Sonu
17PA1A0472
CGI	
 
811	Jampana Sai Deepika
17PA1A0445
CGI	
 
812	Purigalla Sravani
17PA1A0278
CGI	
 
813	Pedapudi Satya Chaithanya Gayathri
17PA1A0273
CGI	
 
814	Veeravalli Vijaya Lakshmi
18PA5A0435
Hexaware	
 
815	Dandabattula Harshith Satya Sai
18PA5A0504
Hexaware	
 
816	Medapati Madhu Bala
18PA5A0422
Hexaware	
 
817	Chinnamsetti L V V Satyanarayana Swamy
18PA5A0406
Hexaware	
 
818	Marripudi Anjani
17PA1A1226
Hexaware	
 
819	Yelamanchili Sunil Kumar
17PA1A05H3
Hexaware	
 
820	Malluru Harshitha
17PA1A0590
Hexaware	
 
821	Anguluri Krupa Jessica
17PA1A0506
Hexaware	
 
822	Annepu Sahasra
17PA1A0507
Hexaware	
 
823	Vulluri Sobha Sudeepthi
17PA1A04H4
Hexaware	
 
824	Yelubandi Naga Manohar
17PA1A04H7
Hexaware	
 
825	Mandavilli Rama Yavanika
17PA1A0490
Hexaware	
 
826	Manam Narayana Rao
17PA1A0487
Hexaware	
 
827	Konapala Bala Siva Prasad
17PA1A0468
Hexaware	
 
828	Konagalla Taruni Sesha Sai
17PA1A0467
Hexaware	
 
829	Yalla Jnaneswari Sri Rama Manimala
17PA1A02B2
Hexaware	
 
830	Grandhi Venkatesh
17PA1A0434
Hexaware	
 
831	Ogirala Sowjanya
17PA1A0268
Hexaware	
 
832	Satyavolu Venkat Sai Charan
17PA1A0288
Hexaware	
 
833	Nulu Jagadeesh Gupta
17PA1A0267
Hexaware	
 
834	Nangineedi Naresh Babu
17PA1A1234
Hexaware	
 
835	Madepalli V V D G Sivanagu
18PA5A0218
Hexaware	
 
836	Shaik Asha
17PA1A04E5
Hexaware	
 
837	Sai Madhuri Kappaganthula
17PA1A04E1
Hexaware	
 
838	Mopidevi Purna
17PA1A0499
Hexaware	
 
839	Rangana Siva Manikanta
17PA1A04D7
Hexaware	
 
840	Kotikalapudi Phaneendra
17PA1A0475
Hexaware	
 
841	Kalidindi Pooja Sahithi
17PA1A0451
Hexaware	
 
842	Akurathi Nikhil
17PA1A0203
Hexaware	
 
843	Garapati Lakshmi Veera Venkata Sairamkumar
17PA1A0430
Hexaware	
 
844	Kothapalli Hanumansatyasuryamanikanta
18PA5A0217
Urjanet	
 
845	Nachu N D V Prasad
17PA1A1231
Urjanet	
 
846	Kundula P S S N V Ravi Kumar
17PA1A0476
Urjanet	
 
847	Likhithapudi Noel
17PA1A0584
Hexaware	
 
848	Nukala Y Ch Mani Rama Naidu
17PA1A05B6
Hexaware	
 
849	Vasa Purna Nagendra Prasad
17PA1A05G5
Hexaware	
 
850	Nammi Venkata Balamurali
17PA1A05A8
Hexaware	
 
851	Grandhi Sri Ram
17PA1A0549
Hexaware	
 
852	Irrinki Neelima Devi
17PA1A0554
Hexaware	
 
853	Sheik Rafi Yerusha
17PA1A04E9
Hexaware	
 
854	Thota Govind Nikhil Durga Naga Kumar
17PA1A04F7
Hexaware	
 
855	Bachu Eswar
17PA1A0408
Hexaware	
 
856	Muppa Bhavana
17PA1A04A6
Hexaware	
 
857	Kallakuri Hari Krishna
19PA1E0018
Cyrrup Solutions Pvt Ltd	
 
858	Nowkatla Harshavardhini
17PA1A1242
Infosys	
 
859	Pindi Prema Saikumar
18PA5A0430
Wipro	
 
860	Yamalavalasa Supriya
18PA5A0437
Infosys	
 
861	Yeluri Bhanu Prakash
17PA1A04H8
CGI	
 
862	Kudipudi Yagna Sree Nagavalli
17PA1A1223
Wipro	
 
863	Anisetti Sai Prudhvi Raj
17PA1A0303
Infosys	
 
864	Kandukuri Anudeep
17PA1A0349
Infosys	
 
865	Danduprolu Ayyappa Vardhan
18PA5A0306
Infosys	
 
866	Dendukuri Venkata Ramaraju
18PA5A0307
Infosys	
 
867	Potturi Murali Krishnam Raju
18PA5A0322
Infosys	
 
868	Vardhineedi Sai Kumari
17PA1A0155
Infosys	
 
869	Jangam Nitin Mourya
17PA1A0339
Infosys	
 
870	Panja Neela Megha Shyam
17PA1A04C0
CGI	
 
871	Hanumanthu Harisha
17PA1A0552
Sonata Software	
 
872	Yeluri Bhanu Prakash
17PA1A04H8
Infosys	
 
873	Koppula Satya Sai Manikanta Kumar
18PA5A0415
Wipro	
 
874	Pindi Prema Saikumar
18PA5A0430
Wipro	
 
875	Bandi Rohith Sainag
17PA1A0206
Wipro	
 
876	Valluri Jaswanth
17PA1A02A5
Wipro	
 
877	Obelisetty V V Gopala Sri Ram Murthy Gupta
17PA1A1244
Wipro	
 
878	Chodavarapu Badrinadh
17PA1A0220
Wipro	
 
879	D Rama Revanth
17PA1A0225
Wipro	
 
880	Annavarapu Narasimha Rao
17PA1A0305
Infosys	
 
881	Peddinti Suryateja
17PA1A0387
Infosys	
 
882	Pulusu Narayana Reddy
17PA1A05D3
Wipro	
 
883	Sanaka Bhargav Ram
17PA1A05E0
Wipro	
 
884	Teki V V V Vijaya Narasimha
17PA1A05F5
Wipro	
 
885	Kondeboina Nagesh Babu
17PA1A0469
Wipro	
 
886	Madda Vijay Ratnam Raju
17PA1A0483
Wipro	
 
887	Marlapudi Dileep
17PA1A0492
Wipro	
 
888	Kondisetti Ramesh
18PA5A0414
Wipro	
 
889	Gajavalli Hara Naga Kesava Gupta
17PA1A0116
Infosys	
 
890	Burela Hitesh Krishna Satya Sai Ram
17PA1A0214
ATOS SYNTEL	
 
891	Talari Srinu Babu
17PA1A0296
TCS NQT - Ninja	
 
892	Nandeti Dimple Sai Venkatesh
17PA1A05A9
Prodapt	
 
893	Nammi Venkata Balamurali
17PA1A05A8
Prodapt	
 
894	Gannamani Siva Sankar
17PA1A0537
Prodapt	
 
895	Puppala Deepak Venkayya Naidu
17PA1A1248
TCS Codevita - Ninja	
 
896	Nekkalapudi Rama Lakshmi
17PA1A1237
TCS Codevita - Ninja	
 
897	Bellamkonda Rohin Surya Prakash
17PA1A1205
TCS Codevita - Ninja	
 
898	Tumpudi Murali Sai Kamal Srikanth
17PA1A05G1
TCS Codevita - Ninja	
 
899	Tummalapalli Venkata Lakshmi Hiranmai
17PA1A05G0
TCS Codevita - Ninja	
 
900	Sayyed Hussain
17PA1A05E4
TCS Codevita - Ninja	
 
901	Penugonda Naga Venkata Raviteja
17PA1A05C6
TCS Codevita - Ninja	
 
902	Peddiboina Krishna Chaitanya
17PA1A05C5
TCS Codevita - Ninja	
 
903	Nittala Lakshmi Sudeepthi
17PA1A05B5
TCS Codevita - Ninja	
 
904	Nimmadhi Jyohi Naga Venkata Siva Sairam
17PA1A05B4
TCS Codevita - Ninja	
 
905	Narina Tharaka Sai Ram
17PA1A05B0
TCS Codevita - Ninja	
 
906	Kone Srimannarayana
17PA1A0577
TCS Codevita - Ninja	
 
907	Kayala Sai Vamsi
17PA1A0570
TCS Codevita - Ninja	
 
908	Kadiyala Hemanth Sai Srinivas
17PA1A0561
TCS Codevita - Ninja	
 
909	Kadali Surya Prakash
17PA1A0559
TCS Codevita - Ninja	
 
910	Grandhi Sri Ram
17PA1A0549
TCS Codevita - Ninja	
 
911	Goriparthi Anvitha
17PA1A0547
TCS Codevita - Ninja	
 
912	Garaga Yathish Bhargav
17PA1A0538
TCS Codevita - Ninja	
 
913	Dirisala Lavanya
17PA1A0531
TCS Codevita - Ninja	
 
914	Choragudi Sai Praveen
17PA1A0524
TCS Codevita - Ninja	
 
915	Bezawada Sadhvi
17PA1A0512
TCS Codevita - Ninja	
 
916	Anguluri Krupa Jessica
17PA1A0506
TCS Codevita - Ninja	
 
917	Sunkavilli Suranya
17PA1A04F2
TCS Codevita - Ninja	
 
918	Pulaparthi Sai Sri
17PA1A04D4
TCS Codevita - Ninja	
 
919	Koppula Jyothi Satya Lakshmi Sai Ajay
17PA1A0471
TCS Codevita - Ninja	
 
920	Jeji Srinivasa Vinnakota
17PA1A0446
TCS Codevita - Ninja	
 
921	Grandhi Venkatesh
17PA1A0434
TCS Codevita - Ninja	
 
922	Garapati Lakshmi Veera Venkata Sairamkumar
17PA1A0430
TCS Codevita - Ninja	
 
923	Dammuluri Yogendra Sai Teja
17PA1A0421
TCS Codevita - Ninja	
 
924	Sankarapu Koteswararao
17PA1A0284
TCS Codevita - Ninja	
 
925	Ravuri Yaswanth Sai Laxman
17PA1A0281
TCS Codevita - Ninja	
 
926	Gundabathula Anusha
17PA1A0232
TCS Codevita - Ninja	
 
927	Bangaru Janaki
17PA1A0207
TCS Codevita - Ninja	
 
928	Abburi Pavani
17PA1A0201
TCS Codevita - Ninja	
 
929	Manda Sai Sri
17PA1A0488
Tech Mahindra	
 
930	Madeti Pavani N S S M K Priyanka
17PA1A0484
Tech Mahindra	
 
931	Nalla Venkata Sai Ram Mohan
17PA1A0266
Tech Mahindra	
 
932	Mekala Yaswanth Reddy
17PA1A0373
MyCaptain	
 
933	Kolla Aravind Babu
17PA1A0123
MyCaptain	
 
934	Penmetsa Satish Varma
17PA1A04C9
Tech Mahindra	
 
935	Chinnamsetti L V V Satyanarayana Swamy
18PA5A0406
Tech Mahindra	
 
936	Peddoju Naga Sai Ganga Chary
18PA5A0429
Tech Mahindra	
 
937	Grandhi Venkatesh
17PA1A0434
Tech Mahindra	
 
938	Sanku Sree Phani Kumar
17PA1A0286
Tech Mahindra	
 
939	Velagala Vember Reddy
17PA1A04H3
Incedo	
 
940	Mukku Bhargavi Devi
17PA1A04A2
ATOS	
 
941	Pindi Prema Saikumar
18PA5A0430
ATOS	
 
942	Lokam Jhnana Reshmika
17PA1A1225
Quest Global	
 
943	Kandula Tejaswini
17PA1A1220
Quest Global	
 
944	Alluri Mydhili Vijaya Lakshmi
19PA1E0002
Rockstar social	
 
945	Guttula Venkata Prudhvi
17PA1A0235
Infosys	
 
946	Potturi Murali Krishnam Raju
18PA5A0322
Delhivery(SCM)	
 
947	Pilaka Suresh
18PA5A0321
Delhivery(SCM)	
 
948	Kanchipogu Vamsi
18PA5A0314
Delhivery(SCM)	
 
949	Anna Sai Manikanta Guptha
18PA5A0301
Delhivery(SCM)	
 
950	Vanga Sai Kondala Satwik
17PA1A03B2
Delhivery(SCM)	
 
951	Budireddy Babu Rao
17PA1A0314
Delhivery(SCM)	
 
952	Sadanala Gana Satya Sai Rajesh
17PA1A0148
Delhivery(SCM)	
 
953	Ganta Naga Durga Rao
18PA5A0308
GESCO Healthcare Pvt. Ltd.	
 
954	Kesireddy Bhargava Venkata Mani Shankar
17PA1A0244
Ngage Technovations LLP	

"""

# pattern = re.compile(r'(\d+)\s+([A-Za-z\s]+)\s+(\w+)\s+([A-Za-z\s]+)\s+Annual Package - (\d+(\.\d+)?) Lakhs')
# pattern = re.compile(r'(\d+)\s+([A-Za-z.\s]+)\s+(\w+)\s+([A-Za-z\s\(\)\[\]\{\}\.\-\&]+)\s+Annual Package - (\d+(\.\d+)?) Lakhs')
pattern = re.compile(r'(\d+)\s+([A-Za-z.\s]+)\s+(\w+)\s+([A-Za-z\s\(\)\[\]\{\}\.\-\&]+)\s')


# Extracting data using regular expressions
matches = pattern.findall(text_data)

# Creating a DataFrame
data = {'S.No': [], 'Name': [], 'Registration Number': [], 'Company': [], 'Package (Lakhs)': []}

for match in matches:
    data['S.No'].append(match[0])
    data['Name'].append(match[1].strip())
    data['Registration Number'].append(match[2])
    data['Company'].append(match[3].strip())
    data['Package (Lakhs)'].append(float(match[4]))

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('2k20-2k21.csv', index=False)

print("CSV file created successfully.")