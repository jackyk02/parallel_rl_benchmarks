import numpy as np
# Sample data representing the logs with training times
logs = """
(base) ubuntu@ip-172-31-74-57:~/benchmarks/rl_example/pong_lf$ python3.9 pong_lf.py
---- Start execution at time Mon Nov 20 07:46:57 2023
---- plus 25882145 nanoseconds
Environment 0: ---- Spawning 8 workers.
Time taken: 2.939258337020874 seconds
Time taken: 3.197274684906006 seconds
Time taken: 3.4467148780822754 seconds
Time taken: 3.5047614574432373 seconds
Time taken: 3.5068914890289307 seconds
Time taken: 4.050273418426514 seconds
Round: 0
Training time: 0.0000 seconds
Reward: -19.0884139401

Time taken: 3.042766809463501 seconds
Time taken: 3.142678737640381 seconds
Time taken: 3.1675868034362793 seconds
Time taken: 3.5675113201141357 seconds
Time taken: 3.8844261169433594 seconds
Time taken: 3.899441957473755 seconds
Round: 1
Training time: 4.0221 seconds
Reward: -19.18027967073248

Time taken: 2.7296831607818604 seconds
Time taken: 3.0585575103759766 seconds
Time taken: 3.0790281295776367 seconds
Time taken: 3.190965175628662 seconds
Time taken: 3.4464681148529053 seconds
Time taken: 4.599357843399048 seconds
Round: 2
Training time: 8.7884 seconds
Reward: -19.23756543253318

Time taken: 3.3036699295043945 seconds
Time taken: 3.4068753719329834 seconds
Time taken: 3.787997245788574 seconds
Time taken: 3.80865740776062 seconds
Time taken: 4.183692932128906 seconds
Time taken: 4.263613939285278 seconds
Round: 3
Training time: 13.1773 seconds
Reward: -19.292280019412853

Time taken: 3.01690411567688 seconds
Time taken: 3.055371046066284 seconds
Time taken: 3.127793312072754 seconds
Time taken: 3.2358314990997314 seconds
Time taken: 3.4043333530426025 seconds
Time taken: 3.8037807941436768 seconds
Round: 4
Training time: 17.1330 seconds
Reward: -19.392215537541745

Time taken: 3.0189173221588135 seconds
Time taken: 3.358278751373291 seconds
Time taken: 3.4729866981506348 seconds
Time taken: 3.5715761184692383 seconds
Time taken: 3.703948974609375 seconds
Time taken: 4.054698467254639 seconds
Round: 5
Training time: 21.3569 seconds
Reward: -19.44728698348119

Time taken: 3.1991374492645264 seconds
Time taken: 3.346846103668213 seconds
Time taken: 3.4738540649414062 seconds
Time taken: 3.5057108402252197 seconds
Time taken: 4.221287488937378 seconds
Time taken: 5.017584323883057 seconds
Round: 6
Training time: 26.5005 seconds
Reward: -19.518641616731998

Time taken: 3.1243245601654053 seconds
Time taken: 3.269639015197754 seconds
Time taken: 3.5018298625946045 seconds
Time taken: 3.575709819793701 seconds
Time taken: 3.5876379013061523 seconds
Time taken: 3.816704273223877 seconds
Round: 7
Training time: 30.4781 seconds
Reward: -19.585727498004417

Time taken: 3.037923812866211 seconds
Time taken: 3.082660436630249 seconds
Time taken: 3.2861552238464355 seconds
Time taken: 3.4117653369903564 seconds
Time taken: 3.616076707839966 seconds
Time taken: 4.154558897018433 seconds
Round: 8
Training time: 34.7640 seconds
Reward: -19.65859051352747

Time taken: 2.9118752479553223 seconds
Time taken: 3.1959774494171143 seconds
Time taken: 3.2882204055786133 seconds
Time taken: 3.639991521835327 seconds
Time taken: 3.658726453781128 seconds
Time taken: 5.179863929748535 seconds
Round: 9
Training time: 40.0946 seconds
Reward: -19.707683636167925

Time taken: 3.193906307220459 seconds
Time taken: 3.3515520095825195 seconds
Time taken: 3.897287130355835 seconds
Time taken: 4.076144218444824 seconds
Time taken: 4.326592683792114 seconds
Time taken: 4.478854656219482 seconds
Round: 10
Training time: 44.7065 seconds
Reward: -19.744295906207018

Time taken: 2.969369649887085 seconds
Time taken: 3.330589771270752 seconds
Time taken: 3.414966106414795 seconds
Time taken: 3.546211004257202 seconds
Time taken: 3.594804525375366 seconds
Time taken: 3.6618363857269287 seconds
Round: 11
Training time: 48.5198 seconds
Reward: -19.78846862167333

Time taken: 3.1065096855163574 seconds
Time taken: 3.1158993244171143 seconds
Time taken: 3.2860233783721924 seconds
Time taken: 3.5604159832000732 seconds
Time taken: 3.7451090812683105 seconds
Time taken: 4.5143091678619385 seconds
Round: 12
Training time: 53.1839 seconds
Reward: -19.830254366430008

Time taken: 3.0035977363586426 seconds
Time taken: 3.2071533203125 seconds
Time taken: 3.272444725036621 seconds
Time taken: 3.299393892288208 seconds
Time taken: 3.326381206512451 seconds
Time taken: 3.5482094287872314 seconds
Round: 13
Training time: 56.8977 seconds
Reward: -19.879101746045357

Time taken: 2.994145154953003 seconds
Time taken: 2.996617555618286 seconds
Time taken: 3.3329155445098877 seconds
Time taken: 3.5847115516662598 seconds
Time taken: 3.7351620197296143 seconds
Time taken: 4.009660482406616 seconds
Round: 14
Training time: 61.0566 seconds
Reward: -19.944696544403467

Time taken: 2.992997884750366 seconds
Time taken: 3.223815679550171 seconds
Time taken: 3.2699456214904785 seconds
Time taken: 3.623655319213867 seconds
Time taken: 4.128672122955322 seconds
Time taken: 4.276836156845093 seconds
Round: 15
Training time: 65.4813 seconds
Reward: -19.937540804861587

Time taken: 2.954033374786377 seconds
Time taken: 3.236973524093628 seconds
Time taken: 3.413747549057007 seconds
Time taken: 3.6471071243286133 seconds
Time taken: 3.7692742347717285 seconds
Time taken: 4.319629192352295 seconds
Round: 16
Training time: 69.9379 seconds
Reward: -19.979914758228624

Time taken: 2.9162678718566895 seconds
Time taken: 2.916783094406128 seconds
Time taken: 3.1017682552337646 seconds
Time taken: 3.2456846237182617 seconds
Time taken: 3.4073474407196045 seconds
Time taken: 3.523397922515869 seconds
Round: 17
Training time: 73.6193 seconds
Reward: -20.02010600417533

Time taken: 2.917074680328369 seconds
Time taken: 3.397326946258545 seconds
Time taken: 3.6747982501983643 seconds
Time taken: 3.787069320678711 seconds
Time taken: 3.8755366802215576 seconds
Time taken: 3.9611101150512695 seconds
Round: 18
Training time: 77.7368 seconds
Reward: -20.07744925441385

Time taken: 3.3066208362579346 seconds
Time taken: 3.331576108932495 seconds
Time taken: 3.353261947631836 seconds
Time taken: 3.606001377105713 seconds
Time taken: 4.096082925796509 seconds
Time taken: 4.404000997543335 seconds
Round: 19
Training time: 82.2910 seconds
Reward: -20.111536786215552

Time taken: 2.9662744998931885 seconds
Time taken: 3.0054726600646973 seconds
Time taken: 3.134446382522583 seconds
Time taken: 3.3425776958465576 seconds
Time taken: 3.8057873249053955 seconds
Time taken: 4.471936225891113 seconds
Round: 20
Training time: 86.9058 seconds
Reward: -20.13392356064893

Time taken: 3.1235511302948 seconds
Time taken: 3.2966175079345703 seconds
Time taken: 3.386734962463379 seconds
Time taken: 3.6521828174591064 seconds
Time taken: 3.8460628986358643 seconds
Time taken: 3.8850584030151367 seconds
Round: 21
Training time: 90.9433 seconds
Reward: -20.16520024448707

Time taken: 3.110140800476074 seconds
Time taken: 3.520132303237915 seconds
Time taken: 3.676638603210449 seconds
Time taken: 3.982426166534424 seconds
Time taken: 4.102704286575317 seconds
Time taken: 4.460976839065552 seconds
Round: 22
Training time: 95.5559 seconds
Reward: -20.155730731159768

Time taken: 2.903045892715454 seconds
Time taken: 2.9271457195281982 seconds
Time taken: 3.348536729812622 seconds
Time taken: 3.6605846881866455 seconds
Time taken: 3.8753695487976074 seconds
Time taken: 4.24233603477478 seconds
Round: 23
Training time: 99.9284 seconds
Reward: -20.146427282537623

Time taken: 2.8753161430358887 seconds
Time taken: 2.9147396087646484 seconds
Time taken: 3.1507480144500732 seconds
Time taken: 3.338218927383423 seconds
Time taken: 3.5736188888549805 seconds
Time taken: 3.7718238830566406 seconds
Round: 24
Training time: 103.8385 seconds
Reward: -20.186478230438908

Time taken: 2.9310829639434814 seconds
Time taken: 3.1362857818603516 seconds
Time taken: 3.3582375049591064 seconds
Time taken: 3.4878180027008057 seconds
Time taken: 3.5796546936035156 seconds
Time taken: 4.586153984069824 seconds
Round: 25
Training time: 108.5897 seconds
Reward: -20.20487842285265

Time taken: 2.973766803741455 seconds
Time taken: 3.656754970550537 seconds
Time taken: 3.841775417327881 seconds
Time taken: 3.8760643005371094 seconds
Time taken: 4.254706144332886 seconds
Time taken: 5.614800930023193 seconds
Round: 26
Training time: 114.3536 seconds
Reward: -20.231904828755358

Time taken: 2.8944082260131836 seconds
Time taken: 2.9178950786590576 seconds
Time taken: 3.225955009460449 seconds
Time taken: 3.3878719806671143 seconds
Time taken: 3.420553684234619 seconds
Time taken: 3.447674512863159 seconds
Round: 27
Training time: 117.9380 seconds
Reward: -20.26695364342241

Time taken: 3.104346513748169 seconds
Time taken: 3.4651412963867188 seconds
Time taken: 3.4966609477996826 seconds
Time taken: 3.6200709342956543 seconds
Time taken: 4.51972770690918 seconds
Time taken: 4.651837587356567 seconds
Round: 28
Training time: 122.7179 seconds
Reward: -20.270740506192475

Time taken: 2.9218435287475586 seconds
Time taken: 2.9567012786865234 seconds
Time taken: 3.092308759689331 seconds
Time taken: 3.3711295127868652 seconds
Time taken: 3.898376226425171 seconds
Time taken: 4.16510796546936 seconds
Round: 29
Training time: 127.0277 seconds
Reward: -20.274598782517995

Time taken: 3.451328754425049 seconds
Time taken: 3.7843198776245117 seconds
Time taken: 3.918208360671997 seconds
Time taken: 4.239275217056274 seconds
Time taken: 4.356201171875 seconds
Time taken: 4.679090976715088 seconds
Round: 30
Training time: 131.8574 seconds
Reward: -20.258922372391375

Time taken: 2.855860471725464 seconds
Time taken: 2.951509714126587 seconds
Time taken: 3.106802225112915 seconds
Time taken: 3.7173843383789062 seconds
Time taken: 3.8656740188598633 seconds
Time taken: 4.029032945632935 seconds
Round: 31
Training time: 136.0370 seconds
Reward: -20.283078204241292

Time taken: 3.1132547855377197 seconds
Time taken: 3.6087541580200195 seconds
Time taken: 3.6539158821105957 seconds
Time taken: 3.9148664474487305 seconds
Time taken: 4.1276819705963135 seconds
Time taken: 4.396068334579468 seconds
Round: 32
Training time: 140.5876 seconds
Reward: -20.286412510021258

Time taken: 2.977491855621338 seconds
Time taken: 3.1253409385681152 seconds
Time taken: 3.1344215869903564 seconds
Time taken: 3.401684522628784 seconds
Time taken: 4.382734775543213 seconds
Time taken: 4.809882879257202 seconds
Round: 33
Training time: 145.5267 seconds
Reward: -20.318468553324134

Time taken: 3.3126440048217773 seconds
Time taken: 3.41477632522583 seconds
Time taken: 3.775864362716675 seconds
Time taken: 3.888625383377075 seconds
Time taken: 4.26192831993103 seconds
Time taken: 4.8635735511779785 seconds
Round: 34
Training time: 150.5493 seconds
Reward: -20.338650671762128

Time taken: 2.8831064701080322 seconds
Time taken: 3.0278122425079346 seconds
Time taken: 3.117835283279419 seconds
Time taken: 3.1180005073547363 seconds
Time taken: 3.192338705062866 seconds
Time taken: 3.554168701171875 seconds
Round: 35
Training time: 154.2460 seconds
Reward: -20.37735273564436

Time taken: 3.424316883087158 seconds
Time taken: 3.494000196456909 seconds
Time taken: 3.5900211334228516 seconds
Time taken: 4.031332015991211 seconds
Time taken: 4.483680248260498 seconds
Time taken: 6.0476319789886475 seconds
Round: 36
Training time: 160.4186 seconds
Reward: -20.335669109931327

Time taken: 3.17297625541687 seconds
Time taken: 3.1920790672302246 seconds
Time taken: 3.220202922821045 seconds
Time taken: 3.479189157485962 seconds
Time taken: 4.738248586654663 seconds
Time taken: 5.169168472290039 seconds
Round: 37
Training time: 165.7516 seconds
Reward: -20.32563767436645

Time taken: 3.3477675914764404 seconds
Time taken: 3.521074056625366 seconds
Time taken: 3.5582048892974854 seconds
Time taken: 3.698054313659668 seconds
Time taken: 4.490279912948608 seconds
Time taken: 4.63669228553772 seconds
Round: 38
Training time: 170.5135 seconds
Reward: -20.335495296812123

Time taken: 3.198227643966675 seconds
Time taken: 3.300342082977295 seconds
Time taken: 3.306490182876587 seconds
Time taken: 3.3320558071136475 seconds
Time taken: 3.665769338607788 seconds
Time taken: 4.030858516693115 seconds
Round: 39
Training time: 174.6900 seconds
Reward: -20.354482012765008

Time taken: 2.9415085315704346 seconds
Time taken: 3.025411367416382 seconds
Time taken: 3.4355993270874023 seconds
Time taken: 3.551896810531616 seconds
Time taken: 3.564749002456665 seconds
Time taken: 4.30929708480835 seconds
Round: 40
Training time: 179.1834 seconds
Reward: -20.372655628936975

Time taken: 3.3155345916748047 seconds
Time taken: 3.570357084274292 seconds
Time taken: 3.5738365650177 seconds
Time taken: 3.67624568939209 seconds
Time taken: 3.889289617538452 seconds
Time taken: 4.486712217330933 seconds
Round: 41
Training time: 183.8110 seconds
Reward: -20.360652837306706

Time taken: 3.126495361328125 seconds
Time taken: 3.3601105213165283 seconds
Time taken: 3.856715679168701 seconds
Time taken: 3.9054794311523438 seconds
Time taken: 4.015777111053467 seconds
Time taken: 4.421494483947754 seconds
Round: 42
Training time: 188.4014 seconds
Reward: -20.368856437249413

Time taken: 3.228405475616455 seconds
Time taken: 3.7777554988861084 seconds
Time taken: 4.202336549758911 seconds
Time taken: 4.4377007484436035 seconds
Time taken: 4.879428148269653 seconds
Time taken: 4.900657415390015 seconds
Round: 43
Training time: 193.4362 seconds
Reward: -20.3476670039481

Time taken: 3.121448278427124 seconds
Time taken: 3.3628828525543213 seconds
Time taken: 3.3770546913146973 seconds
Time taken: 3.431835651397705 seconds
Time taken: 3.43904972076416 seconds
Time taken: 4.76665472984314 seconds
Round: 44
Training time: 198.3352 seconds
Reward: -20.36623943341786

Time taken: 3.2035491466522217 seconds
Time taken: 3.374175548553467 seconds
Time taken: 3.3840065002441406 seconds
Time taken: 3.449150800704956 seconds
Time taken: 3.948538303375244 seconds
Time taken: 4.868677854537964 seconds
Round: 45
Training time: 203.3512 seconds
Reward: -20.38382104698979

Time taken: 3.0115041732788086 seconds
Time taken: 3.20119571685791 seconds
Time taken: 3.4748830795288086 seconds
Time taken: 3.6897621154785156 seconds
Time taken: 3.826093912124634 seconds
Time taken: 4.544170141220093 seconds
Round: 46
Training time: 208.0462 seconds
Reward: -20.3708638866632

Time taken: 3.218374729156494 seconds
Time taken: 3.223369836807251 seconds
Time taken: 3.684957504272461 seconds
Time taken: 3.9378557205200195 seconds
Time taken: 4.196716547012329 seconds
Time taken: 4.517854690551758 seconds
Round: 47
Training time: 212.6956 seconds
Reward: -20.378568917822104

Time taken: 2.987609624862671 seconds
Time taken: 3.0816261768341064 seconds
Time taken: 3.0850038528442383 seconds
Time taken: 3.14997935295105 seconds
Time taken: 3.8378982543945312 seconds
Time taken: 3.986926794052124 seconds
Round: 48
Training time: 216.8536 seconds
Reward: -20.414934971908732

Time taken: 3.3694748878479004 seconds
Time taken: 3.431394338607788 seconds
Time taken: 3.479937791824341 seconds
Time taken: 4.075525999069214 seconds
Time taken: 4.439294338226318 seconds
Time taken: 4.801966905593872 seconds
Round: 49
Training time: 221.7919 seconds
Reward: -20.40025700944434

Time taken: 3.1106796264648438 seconds
Time taken: 3.296738862991333 seconds
Time taken: 3.32460880279541 seconds
Time taken: 3.4090819358825684 seconds
Time taken: 3.8361175060272217 seconds
Time taken: 4.294370412826538 seconds
Round: 50
Training time: 226.2369 seconds
Reward: -20.41594789964946

Time taken: 3.0062437057495117 seconds
Time taken: 3.3436965942382812 seconds
Time taken: 3.5590052604675293 seconds
Time taken: 3.6039340496063232 seconds
Time taken: 3.6630311012268066 seconds
Time taken: 4.2803425788879395 seconds
Round: 51
Training time: 230.6393 seconds
Reward: -20.44061664080501

Time taken: 2.973187208175659 seconds
Time taken: 3.397007942199707 seconds
Time taken: 3.752764940261841 seconds
Time taken: 3.8026671409606934 seconds
Time taken: 3.87603497505188 seconds
Time taken: 4.300016164779663 seconds
Round: 52
Training time: 235.1190 seconds
Reward: -20.414833810813676

Time taken: 3.1402554512023926 seconds
Time taken: 3.163530111312866 seconds
Time taken: 3.328105926513672 seconds
Time taken: 3.604792356491089 seconds
Time taken: 4.0448267459869385 seconds
Time taken: 4.749557971954346 seconds
Round: 53
Training time: 240.0033 seconds
Reward: -20.429573658780445

Time taken: 3.2272515296936035 seconds
Time taken: 3.429142951965332 seconds
Time taken: 3.436215400695801 seconds
Time taken: 3.474989652633667 seconds
Time taken: 3.5200512409210205 seconds
Time taken: 4.033032178878784 seconds
Round: 54
Training time: 244.1919 seconds
Reward: -20.443547962946347

Time taken: 3.2043263912200928 seconds
Time taken: 3.5111451148986816 seconds
Time taken: 3.6146583557128906 seconds
Time taken: 3.786186695098877 seconds
Time taken: 3.811228036880493 seconds
Time taken: 4.5056235790252686 seconds
Round: 55
Training time: 248.8472 seconds
Reward: -20.436999552521236

Time taken: 2.865102529525757 seconds
Time taken: 2.9039268493652344 seconds
Time taken: 3.454346179962158 seconds
Time taken: 3.7260327339172363 seconds
Time taken: 3.9522910118103027 seconds
Time taken: 4.065622568130493 seconds
Round: 56
Training time: 253.0547 seconds
Reward: -20.450536354095867

Time taken: 3.0974934101104736 seconds
Time taken: 3.263554811477661 seconds
Time taken: 3.483295202255249 seconds
Time taken: 3.8935983180999756 seconds
Time taken: 4.221338987350464 seconds
Time taken: 4.449348211288452 seconds
Round: 57
Training time: 257.6564 seconds
Reward: -20.44328689456375

Time taken: 2.973402261734009 seconds
Time taken: 3.3973495960235596 seconds
Time taken: 3.7815074920654297 seconds
Time taken: 4.0208234786987305 seconds
Time taken: 4.582695007324219 seconds
Time taken: 4.679747581481934 seconds
Round: 58
Training time: 262.4809 seconds
Reward: -20.475865662320388

Time taken: 3.0154306888580322 seconds
Time taken: 3.2796037197113037 seconds
Time taken: 3.331897258758545 seconds
Time taken: 3.6803650856018066 seconds
Time taken: 4.1113440990448 seconds
Time taken: 4.256221532821655 seconds
Round: 59
Training time: 266.8675 seconds
Reward: -20.486736925455205

Time taken: 3.1692073345184326 seconds
Time taken: 3.346036672592163 seconds
Time taken: 3.6114819049835205 seconds
Time taken: 3.6516525745391846 seconds
Time taken: 3.6682262420654297 seconds
Time taken: 4.173497438430786 seconds
Round: 60
Training time: 271.1879 seconds
Reward: -20.506873003895553

Time taken: 2.903960943222046 seconds
Time taken: 3.0032756328582764 seconds
Time taken: 3.1227831840515137 seconds
Time taken: 3.9325902462005615 seconds
Time taken: 4.1034650802612305 seconds
Time taken: 4.365489959716797 seconds
Round: 61
Training time: 275.6795 seconds
Reward: -20.526124761933918

Time taken: 3.2057719230651855 seconds
Time taken: 3.527743339538574 seconds
Time taken: 3.7961602210998535 seconds
Time taken: 3.8562440872192383 seconds
Time taken: 3.87833571434021 seconds
Time taken: 4.010356187820435 seconds
Round: 62
Training time: 279.8228 seconds
Reward: -20.524349909968105

Time taken: 2.994124174118042 seconds
Time taken: 3.088517189025879 seconds
Time taken: 3.119565725326538 seconds
Time taken: 3.2399537563323975 seconds
Time taken: 3.261138439178467 seconds
Time taken: 3.5561203956604004 seconds
Round: 63
Training time: 283.5171 seconds
Reward: -20.513758121076176

Time taken: 3.1189942359924316 seconds
Time taken: 3.572124719619751 seconds
Time taken: 3.5739858150482178 seconds
Time taken: 3.611497402191162 seconds
Time taken: 3.7371294498443604 seconds
Time taken: 4.090435981750488 seconds
Round: 64
Training time: 287.7527 seconds
Reward: -20.51270893318577

Time taken: 3.150118350982666 seconds
Time taken: 3.241126775741577 seconds
Time taken: 3.261157751083374 seconds
Time taken: 3.368833541870117 seconds
Time taken: 3.8332841396331787 seconds
Time taken: 4.024176597595215 seconds
Round: 65
Training time: 291.9076 seconds
Reward: -20.502109273014966

Time taken: 2.8952410221099854 seconds
Time taken: 3.350900650024414 seconds
Time taken: 3.632350206375122 seconds
Time taken: 3.6469521522521973 seconds
Time taken: 4.233238935470581 seconds
Time taken: 4.549734830856323 seconds
Round: 66
Training time: 296.6006 seconds
Reward: -20.49223284377276

Time taken: 3.172433853149414 seconds
Time taken: 3.3595786094665527 seconds
Time taken: 3.4761464595794678 seconds
Time taken: 3.612426280975342 seconds
Time taken: 4.266856670379639 seconds
Time taken: 4.511660814285278 seconds
Round: 67
Training time: 301.2513 seconds
Reward: -20.492540341794257

Time taken: 3.1556029319763184 seconds
Time taken: 3.4911224842071533 seconds
Time taken: 3.5151467323303223 seconds
Time taken: 3.5195555686950684 seconds
Time taken: 3.583400249481201 seconds
Time taken: 4.340749979019165 seconds
Round: 68
Training time: 305.7256 seconds
Reward: -20.502630845077476

Time taken: 3.2046146392822266 seconds
Time taken: 3.475301742553711 seconds
Time taken: 3.5972740650177 seconds
Time taken: 3.754288673400879 seconds
Time taken: 3.7603347301483154 seconds
Time taken: 3.9604501724243164 seconds
Round: 69
Training time: 309.8574 seconds
Reward: -20.502330853616094

Time taken: 2.9656026363372803 seconds
Time taken: 3.1247756481170654 seconds
Time taken: 3.5708963871002197 seconds
Time taken: 3.921818256378174 seconds
Time taken: 4.171199321746826 seconds
Time taken: 4.338368892669678 seconds
Round: 70
Training time: 314.3304 seconds
Reward: -20.492634576712216

Time taken: 2.9610087871551514 seconds
Time taken: 3.681217670440674 seconds
Time taken: 3.861362934112549 seconds
Time taken: 4.129299163818359 seconds
Time taken: 4.174410343170166 seconds
Time taken: 4.274287223815918 seconds
Round: 71
Training time: 318.7711 seconds
Reward: -20.482724525482116

Time taken: 3.305816411972046 seconds
Time taken: 3.331235647201538 seconds
Time taken: 3.332097053527832 seconds
Time taken: 3.550387382507324 seconds
Time taken: 4.07384467124939 seconds
Time taken: 4.7667317390441895 seconds
Round: 72
Training time: 323.6678 seconds
Reward: -20.483879548370428

Time taken: 3.599775791168213 seconds
Time taken: 3.792327642440796 seconds
Time taken: 3.8314335346221924 seconds
Time taken: 4.256110191345215 seconds
Time taken: 4.274173974990845 seconds
Time taken: 4.45935583114624 seconds
Round: 73
Training time: 328.2779 seconds
Reward: -20.504182840090877

Time taken: 2.6620655059814453 seconds
Time taken: 3.364800453186035 seconds
Time taken: 3.6229159832000732 seconds
Time taken: 3.810032606124878 seconds
Time taken: 4.046436309814453 seconds
Time taken: 4.4696197509765625 seconds
Round: 74
Training time: 332.8884 seconds
Reward: -20.503892006213185

Time taken: 3.094803810119629 seconds
Time taken: 3.231955051422119 seconds
Time taken: 3.4466969966888428 seconds
Time taken: 3.623004913330078 seconds
Time taken: 3.8512933254241943 seconds
Time taken: 4.296621561050415 seconds
Round: 75
Training time: 337.3289 seconds
Reward: -20.503420181890558

Time taken: 3.163233757019043 seconds
Time taken: 3.2943074703216553 seconds
Time taken: 3.548487663269043 seconds
Time taken: 3.9583184719085693 seconds
Time taken: 4.644280910491943 seconds
Time taken: 4.907165765762329 seconds
Round: 76
Training time: 342.4012 seconds
Reward: -20.4935650484568

Time taken: 2.994734764099121 seconds
Time taken: 3.30672025680542 seconds
Time taken: 3.6506381034851074 seconds
Time taken: 3.65639591217041 seconds
Time taken: 3.8890585899353027 seconds
Time taken: 4.161932468414307 seconds
Round: 77
Training time: 346.6960 seconds
Reward: -20.49408568556022

Time taken: 3.04461407661438 seconds
Time taken: 3.0889604091644287 seconds
Time taken: 3.108045816421509 seconds
Time taken: 3.142869710922241 seconds
Time taken: 3.782214403152466 seconds
Time taken: 4.23310112953186 seconds
Round: 78
Training time: 351.0776 seconds
Reward: -20.51408575555713

Time taken: 3.1592867374420166 seconds
Time taken: 3.1640422344207764 seconds
Time taken: 3.180401563644409 seconds
Time taken: 3.3628990650177 seconds
Time taken: 3.508291721343994 seconds
Time taken: 4.268103361129761 seconds
Round: 79
Training time: 355.4805 seconds
Reward: -20.532915424445857

Time taken: 2.909393787384033 seconds
Time taken: 3.0881736278533936 seconds
Time taken: 3.2477715015411377 seconds
Time taken: 3.7855734825134277 seconds
Time taken: 3.87164044380188 seconds
Time taken: 4.088135242462158 seconds
Round: 80
Training time: 359.7498 seconds
Reward: -20.53103824352538

Time taken: 3.3089728355407715 seconds
Time taken: 3.317371129989624 seconds
Time taken: 3.810600996017456 seconds
Time taken: 4.062774658203125 seconds
Time taken: 4.632766485214233 seconds
Time taken: 5.16180682182312 seconds
Round: 81
Training time: 365.0394 seconds
Reward: -20.50015897485192

Time taken: 2.849153995513916 seconds
Time taken: 2.966355800628662 seconds
Time taken: 3.003679037094116 seconds
Time taken: 3.251352310180664 seconds
Time taken: 3.634160280227661 seconds
Time taken: 3.677276849746704 seconds
Round: 82
Training time: 368.8875 seconds
Reward: -20.500492736367836

Time taken: 3.14009690284729 seconds
Time taken: 3.429417610168457 seconds
Time taken: 3.6849327087402344 seconds
Time taken: 3.9663636684417725 seconds
Time taken: 4.2657458782196045 seconds
Time taken: 4.704393148422241 seconds
Round: 83
Training time: 373.7461 seconds
Reward: -20.471011886708705

Time taken: 3.1744234561920166 seconds
Time taken: 3.417306423187256 seconds
Time taken: 3.637338161468506 seconds
Time taken: 3.6744937896728516 seconds
Time taken: 3.8887338638305664 seconds
Time taken: 4.711495876312256 seconds
Round: 84
Training time: 378.6020 seconds
Reward: -20.452955301568156

Time taken: 2.831369638442993 seconds
Time taken: 3.403402328491211 seconds
Time taken: 3.434126853942871 seconds
Time taken: 3.4574644565582275 seconds
Time taken: 3.621608257293701 seconds
Time taken: 3.9277467727661133 seconds
Round: 85
Training time: 382.6759 seconds
Reward: -20.455462315491364

Time taken: 2.940331220626831 seconds
Time taken: 3.2048988342285156 seconds
Time taken: 3.290250778198242 seconds
Time taken: 3.305785655975342 seconds
Time taken: 3.406073570251465 seconds
Time taken: 3.6759848594665527 seconds
Round: 86
Training time: 386.4812 seconds
Reward: -20.457818678935336

Time taken: 3.0953757762908936 seconds
Time taken: 3.204432964324951 seconds
Time taken: 3.2164645195007324 seconds
Time taken: 3.4933135509490967 seconds
Time taken: 3.661675453186035 seconds
Time taken: 4.807331085205078 seconds
Round: 87
Training time: 391.4405 seconds
Reward: -20.47023614834261

Time taken: 2.9193639755249023 seconds
Time taken: 3.1609883308410645 seconds
Time taken: 3.4504222869873047 seconds
Time taken: 4.454086542129517 seconds
Time taken: 4.751163005828857 seconds
Time taken: 5.973423957824707 seconds
Round: 88
Training time: 397.5402 seconds
Reward: -20.452522939594356

Time taken: 3.0916907787323 seconds
Time taken: 3.2272791862487793 seconds
Time taken: 3.2632222175598145 seconds
Time taken: 3.3293650150299072 seconds
Time taken: 3.54291033744812 seconds
Time taken: 3.6363942623138428 seconds
Round: 89
Training time: 401.3146 seconds
Reward: -20.45564435477667

Time taken: 3.0312211513519287 seconds
Time taken: 3.275883436203003 seconds
Time taken: 3.6495745182037354 seconds
Time taken: 3.7760610580444336 seconds
Time taken: 3.8341658115386963 seconds
Time taken: 4.170620918273926 seconds
Round: 90
Training time: 405.6421 seconds
Reward: -20.477796975807866

Time taken: 3.5133345127105713 seconds
Time taken: 3.5688467025756836 seconds
Time taken: 3.7444143295288086 seconds
Time taken: 3.767134189605713 seconds
Time taken: 4.172943353652954 seconds
Time taken: 4.200176477432251 seconds
Round: 91
Training time: 409.9818 seconds
Reward: -20.489047268665935

Time taken: 3.3487908840179443 seconds
Time taken: 3.668858528137207 seconds
Time taken: 3.746843099594116 seconds
Time taken: 4.234648704528809 seconds
Time taken: 4.558976411819458 seconds
Time taken: 4.933313608169556 seconds
Round: 92
Training time: 415.0542 seconds
Reward: -20.460824285866757

Time taken: 2.983379364013672 seconds
Time taken: 3.200824022293091 seconds
Time taken: 3.497284173965454 seconds
Time taken: 3.6417012214660645 seconds
Time taken: 5.059744119644165 seconds
Time taken: 5.085451364517212 seconds
Round: 93
Training time: 420.2802 seconds
Reward: -20.40357177810444

Time taken: 2.8715741634368896 seconds
Time taken: 2.9913759231567383 seconds
Time taken: 3.0899603366851807 seconds
Time taken: 3.1102471351623535 seconds
Time taken: 3.6258411407470703 seconds
Time taken: 3.990957498550415 seconds
Round: 94
Training time: 424.4150 seconds
Reward: -20.4384746685428

Time taken: 2.9560203552246094 seconds
Time taken: 3.0768377780914307 seconds
Time taken: 3.080349922180176 seconds
Time taken: 3.714294910430908 seconds
Time taken: 3.9366660118103027 seconds
Time taken: 4.590857028961182 seconds
Round: 95
Training time: 429.1567 seconds
Reward: -20.46133504704723

Time taken: 3.009279251098633 seconds
Time taken: 3.186527967453003 seconds
Time taken: 3.1980080604553223 seconds
Time taken: 3.250953435897827 seconds
Time taken: 3.326780319213867 seconds
Time taken: 3.712519884109497 seconds
Round: 96
Training time: 433.0093 seconds
Reward: -20.46344773911794

Time taken: 3.114056348800659 seconds
Time taken: 3.265794277191162 seconds
Time taken: 3.448676109313965 seconds
Time taken: 4.145265340805054 seconds
Time taken: 4.1562933921813965 seconds
Time taken: 4.31329345703125 seconds
Round: 97
Training time: 437.4920 seconds
Reward: -20.48484669726331

Time taken: 2.9846858978271484 seconds
Time taken: 3.1028871536254883 seconds
Time taken: 3.3041563034057617 seconds
Time taken: 3.5023305416107178 seconds
Time taken: 3.711773633956909 seconds
Time taken: 4.088521242141724 seconds
Round: 98
Training time: 441.7181 seconds
Reward: -20.49538743147504

Time taken: 2.971599817276001 seconds
Time taken: 3.2334132194519043 seconds
Time taken: 3.4195423126220703 seconds
Time taken: 3.4209790229797363 seconds
Time taken: 4.044679403305054 seconds
Time taken: 4.538487672805786 seconds
Round: 99
Training time: 446.3788 seconds
Reward: -20.505510323495503

Time taken: 3.4642398357391357 seconds
Time taken: 3.516789197921753 seconds
Time taken: 3.773817777633667 seconds
Time taken: 3.7883315086364746 seconds
Time taken: 3.871367931365967 seconds
Time taken: 3.950566053390503 seconds
Round: 100
Training time: 450.5008 seconds
Reward: -20.495825964788295

Time taken: 2.8988959789276123 seconds
Time taken: 2.9627373218536377 seconds
Time taken: 3.63364839553833 seconds
Time taken: 3.734315872192383 seconds
Time taken: 3.97343373298645 seconds
Time taken: 4.081979990005493 seconds
Round: 101
Training time: 454.7448 seconds
Reward: -20.476223193904783

Time taken: 3.1649856567382812 seconds
Time taken: 3.2448294162750244 seconds
Time taken: 3.2918753623962402 seconds
Time taken: 3.595186233520508 seconds
Time taken: 3.8877828121185303 seconds
Time taken: 4.589165210723877 seconds
Round: 102
Training time: 459.4871 seconds
Reward: -20.477468554344703

Time taken: 3.083137273788452 seconds
Time taken: 3.2029078006744385 seconds
Time taken: 3.4175264835357666 seconds
Time taken: 3.5715208053588867 seconds
Time taken: 3.708601474761963 seconds
Time taken: 4.272876977920532 seconds
Round: 103
Training time: 463.9082 seconds
Reward: -20.459428136177735

Time taken: 2.854048728942871 seconds
Time taken: 2.9637134075164795 seconds
Time taken: 3.1560020446777344 seconds
Time taken: 3.344264030456543 seconds
Time taken: 4.332968711853027 seconds
Time taken: 4.366855621337891 seconds
Round: 104
Training time: 468.4142 seconds
Reward: -20.461062320886636

Time taken: 3.2655282020568848 seconds
Time taken: 3.2786145210266113 seconds
Time taken: 3.418308973312378 seconds
Time taken: 3.836604118347168 seconds
Time taken: 3.888887882232666 seconds
Time taken: 4.462069272994995 seconds
Round: 105
Training time: 473.0277 seconds
Reward: -20.453493893350522

Time taken: 3.409695863723755 seconds
Time taken: 3.4469454288482666 seconds
Time taken: 3.572265625 seconds
Time taken: 3.6482527256011963 seconds
Time taken: 3.7023086547851562 seconds
Time taken: 3.9834678173065186 seconds
Round: 106
Training time: 477.1471 seconds
Reward: -20.465674349063093

Time taken: 3.196707010269165 seconds
Time taken: 3.286762237548828 seconds
Time taken: 3.590627670288086 seconds
Time taken: 3.8471357822418213 seconds
Time taken: 3.9765031337738037 seconds
Time taken: 4.026552438735962 seconds
Round: 107
Training time: 481.3512 seconds
Reward: -20.47792320532914

Time taken: 3.673502206802368 seconds
Time taken: 3.742203950881958 seconds
Time taken: 3.7980501651763916 seconds
Time taken: 4.044223070144653 seconds
Time taken: 4.053325176239014 seconds
Time taken: 4.2289299964904785 seconds
Round: 108
Training time: 485.7225 seconds
Reward: -20.46985521075549

Time taken: 3.117704391479492 seconds
Time taken: 3.258358955383301 seconds
Time taken: 3.4054341316223145 seconds
Time taken: 3.4762821197509766 seconds
Time taken: 3.6173417568206787 seconds
Time taken: 4.221948623657227 seconds
Round: 109
Training time: 490.0935 seconds
Reward: -20.47147322461792

Time taken: 3.1606452465057373 seconds
Time taken: 3.3621890544891357 seconds
Time taken: 3.5425796508789062 seconds
Time taken: 3.5523664951324463 seconds
Time taken: 3.6894330978393555 seconds
Time taken: 3.7181873321533203 seconds
Round: 110
Training time: 493.9535 seconds
Reward: -20.443588642051843

Time taken: 3.3562228679656982 seconds
Time taken: 3.5140256881713867 seconds
Time taken: 3.583326578140259 seconds
Time taken: 4.000784397125244 seconds
Time taken: 4.124179363250732 seconds
Time taken: 4.296143531799316 seconds
Round: 111
Training time: 498.3867 seconds
Reward: -20.417532871091552

Time taken: 3.2583391666412354 seconds
Time taken: 3.451995611190796 seconds
Time taken: 3.5634899139404297 seconds
Time taken: 3.6748926639556885 seconds
Time taken: 3.7397191524505615 seconds
Time taken: 4.363537311553955 seconds
Round: 112
Training time: 502.8994 seconds
Reward: -20.451618760454107

Time taken: 2.804352283477783 seconds
Time taken: 2.92429518699646 seconds
Time taken: 3.226222515106201 seconds
Time taken: 3.4167728424072266 seconds
Time taken: 3.7807109355926514 seconds
Time taken: 3.840369701385498 seconds
Round: 113
Training time: 506.8984 seconds
Reward: -20.46410695866363

Time taken: 3.2271320819854736 seconds
Time taken: 3.8327038288116455 seconds
Time taken: 4.049986124038696 seconds
Time taken: 4.204665184020996 seconds
Time taken: 4.244940996170044 seconds
Time taken: 4.2814741134643555 seconds
Round: 114
Training time: 511.3207 seconds
Reward: -20.456937637882678

Time taken: 3.155290126800537 seconds
Time taken: 3.1943626403808594 seconds
Time taken: 3.2014577388763428 seconds
Time taken: 3.2376089096069336 seconds
Time taken: 3.422032594680786 seconds
Time taken: 3.834488868713379 seconds
Round: 115
Training time: 515.3238 seconds
Reward: -20.44921160607972

Time taken: 3.0459063053131104 seconds
Time taken: 3.4413750171661377 seconds
Time taken: 3.552682638168335 seconds
Time taken: 3.5870866775512695 seconds
Time taken: 4.850212335586548 seconds
Time taken: 5.146491289138794 seconds
Round: 116
Training time: 520.6114 seconds
Reward: -20.4518406706036

Time taken: 2.831958055496216 seconds
Time taken: 3.165682554244995 seconds
Time taken: 3.7972733974456787 seconds
Time taken: 3.9018008708953857 seconds
Time taken: 3.935519218444824 seconds
Time taken: 4.537160873413086 seconds
Round: 117
Training time: 525.3108 seconds
Reward: -20.444414882664322

Time taken: 3.656343936920166 seconds
Time taken: 3.6779208183288574 seconds
Time taken: 3.9691593647003174 seconds
Time taken: 4.07723069190979 seconds
Time taken: 4.373517036437988 seconds
Time taken: 5.185316562652588 seconds
Round: 118
Training time: 530.6217 seconds
Reward: -20.409096869926834

Time taken: 2.9447035789489746 seconds
Time taken: 3.0745656490325928 seconds
Time taken: 3.2816667556762695 seconds
Time taken: 3.4633359909057617 seconds
Time taken: 3.528790235519409 seconds
Time taken: 3.6827211380004883 seconds
Round: 119
Training time: 534.4394 seconds
Reward: -20.4338754328172

Time taken: 3.3829073905944824 seconds
Time taken: 3.5941145420074463 seconds
Time taken: 3.6184799671173096 seconds
Time taken: 3.8085873126983643 seconds
Time taken: 3.9281344413757324 seconds
Time taken: 4.461410284042358 seconds
Round: 120
Training time: 539.0539 seconds
Reward: -20.427602957909162

Time taken: 2.9276623725891113 seconds
Time taken: 2.941699504852295 seconds
Time taken: 3.4976112842559814 seconds
Time taken: 3.71726393699646 seconds
Time taken: 3.8774290084838867 seconds
Time taken: 4.272963762283325 seconds
Round: 121
Training time: 543.4891 seconds
Reward: -20.41237772659663

Time taken: 2.832225799560547 seconds
Time taken: 3.1767618656158447 seconds
Time taken: 3.205536127090454 seconds
Time taken: 3.2085297107696533 seconds
Time taken: 3.2357985973358154 seconds
Time taken: 4.576487064361572 seconds
Round: 122
Training time: 548.2091 seconds
Reward: -20.427553374044848

Time taken: 3.1731550693511963 seconds
Time taken: 3.227889060974121 seconds
Time taken: 3.314765214920044 seconds
Time taken: 3.708861827850342 seconds
Time taken: 4.243898868560791 seconds
Time taken: 5.145078420639038 seconds
Round: 123
Training time: 553.5134 seconds
Reward: -20.421451865071646

Time taken: 3.0411312580108643 seconds
Time taken: 3.2459769248962402 seconds
Time taken: 3.3360118865966797 seconds
Time taken: 3.6881048679351807 seconds
Time taken: 3.7867112159729004 seconds
Time taken: 4.58381986618042 seconds
Round: 124
Training time: 558.2316 seconds
Reward: -20.416398445491986

Time taken: 3.317270517349243 seconds
Time taken: 3.5992958545684814 seconds
Time taken: 3.675156593322754 seconds
Time taken: 3.7889373302459717 seconds
Time taken: 4.168220043182373 seconds
Time taken: 4.627654552459717 seconds
Round: 125
Training time: 562.9959 seconds
Reward: -20.411341771171138

Time taken: 3.128364086151123 seconds
Time taken: 3.4333579540252686 seconds
Time taken: 3.43992280960083 seconds
Time taken: 3.5196189880371094 seconds
Time taken: 3.6779208183288574 seconds
Time taken: 4.288683176040649 seconds
Round: 126
Training time: 567.4341 seconds
Reward: -20.43608697277608

Time taken: 3.27101731300354 seconds
Time taken: 3.382272243499756 seconds
Time taken: 3.469020366668701 seconds
Time taken: 3.758835792541504 seconds
Time taken: 3.874171018600464 seconds
Time taken: 4.549584150314331 seconds
Round: 127
Training time: 572.1285 seconds
Reward: -20.43987911878006

Time taken: 2.9428977966308594 seconds
Time taken: 2.95827054977417 seconds
Time taken: 3.150303363800049 seconds
Time taken: 3.3892838954925537 seconds
Time taken: 3.49859356880188 seconds
Time taken: 4.254543304443359 seconds
Round: 128
Training time: 576.5376 seconds
Reward: -20.463051348966435

Time taken: 2.9144184589385986 seconds
Time taken: 3.2450122833251953 seconds
Time taken: 3.2803118228912354 seconds
Time taken: 3.32840633392334 seconds
Time taken: 3.829045057296753 seconds
Time taken: 4.66656231880188 seconds
Round: 129
Training time: 581.3425 seconds
Reward: -20.465654653205256

Time taken: 3.0399062633514404 seconds
Time taken: 3.156045436859131 seconds
Time taken: 3.619339942932129 seconds
Time taken: 3.7406249046325684 seconds
Time taken: 3.8854219913482666 seconds
Time taken: 4.069678783416748 seconds
Round: 130
Training time: 585.5519 seconds
Reward: -20.438507552867957

Time taken: 2.8649706840515137 seconds
Time taken: 3.081861972808838 seconds
Time taken: 3.2474496364593506 seconds
Time taken: 3.3114707469940186 seconds
Time taken: 3.36891770362854 seconds
Time taken: 3.642584800720215 seconds
Round: 131
Training time: 589.3530 seconds
Reward: -20.422260016986588

Time taken: 2.9123876094818115 seconds
Time taken: 3.174210786819458 seconds
Time taken: 3.2617452144622803 seconds
Time taken: 3.4014039039611816 seconds
Time taken: 3.4165961742401123 seconds
Time taken: 3.939878463745117 seconds
Round: 132
Training time: 593.4311 seconds
Reward: -20.4366593739786

Time taken: 3.2525367736816406 seconds
Time taken: 3.578399896621704 seconds
Time taken: 3.9492733478546143 seconds
Time taken: 4.319979667663574 seconds
Time taken: 4.335572004318237 seconds
Time taken: 5.481101036071777 seconds
Round: 133
Training time: 599.0460 seconds
Reward: -20.42041309275072

Time taken: 2.920909881591797 seconds
Time taken: 3.403817892074585 seconds
Time taken: 3.5529797077178955 seconds
Time taken: 3.5680532455444336 seconds
Time taken: 3.8128275871276855 seconds
Time taken: 4.353052616119385 seconds
Round: 134
Training time: 603.5214 seconds
Reward: -20.434826441972085
"""

# Split the logs into lines, then filter and process lines containing "Training time"
training_times = [float(line.split(": ")[1].split(" ")[0])
                  for line in logs.split("\n")
                  if "Training time" in line]

# Calculate differences between consecutive training times
time_differences = [round(training_times[i] - training_times[i - 1], 4)
                    for i in range(1, len(training_times))]

print(time_differences)
print(np.mean(time_differences))
