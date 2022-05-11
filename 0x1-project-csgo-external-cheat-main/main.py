import os
import pymem
import pymem.process
import keyboard
import time
import random

# config
from config import *

# functions
from functions.manager import *
from functions.aimbot import *
from functions.bhop import *
from functions.triggerbot import *
from functions.glow import *
from functions.wireframe import *
from functions.chams import *
from functions.rcs import *
from functions.junkcode import *
from functions.noflash import *
from functions.radar import *
from functions.fov import *

# offsets
from offsets.autoUpdater import *
from offsets.offsets import *

os.system("cls")
print("[maybach.wtf]: Update cheat bypass...")
junkcode()

print("[maybach.wtf]: Updating offets...")
update()

glowActive = False
chamsActive = False
rcsActive = False
aimActive = False
wireActive = False
noFlashActive = False
radarActive = False
fovedAc = True


def main():
    print("[maybach.wtf]: Finding csgo.exe ...")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)

    print("[maybach.wtf]: Injected!")

    global glowActive
    global chamsActive
    global rcsActive
    global aimActive
    global wireActive
    global noFlashActive
    global radarActive
    global fovedAc

    os.system("cls")
    print("Welcome to maybach.wtf")
    print("Coded by: ｖｏｉｄ#3603")
    print("\n \nHotkeys:")
    print("----------[Hold]----------")
    print("Radar: Shift")
    print("Bhop: Space")
    print("TriggerBot: Alt")
    print("----------[Toggle]----------")
    print("Glow: F6")
    print("Chams visible: F7")
    print("RCS: F8")
    print("Aimbot: F9, C key to use")
    print("No FLash: F11")
    print("Wireframe: F10")
    print("Fov: Press '-' to make less fov or '+' to make more fov")
    print("\n----------[Console]----------")
    print("\n \nLogs:")

    while True:

        manager(pm, client, engine, enginePointer)
        bhop(pm, client, engine, enginePointer)
        trigger(pm, client, engine, enginePointer, triggerbotDelay)

        # glow
        if keyboard.is_pressed("F6") and glowActive is False:
            glowActive = True
            print("[maybach.wtf]: Glow active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F6") and glowActive is True:
            glowActive = False
            print("[maybach.wtf]: Glow no active")
            time.sleep(0.2)

        if (glowActive):
            glow(pm, client, engine, enginePointer)

        # rcs
        if keyboard.is_pressed("F8") and rcsActive is False:
            rcsActive = True
            print("[maybach.wtf]: rcs active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F8") and rcsActive is True:
            rcsActive = False
            print("[maybach.wtf]: rcs no active")
            time.sleep(0.2)

        if (rcsActive):
            rcs(pm, client, engine, enginePointer)

        # chams
        if keyboard.is_pressed("F7") and chamsActive is False:
            chamsActive = True
            print("[maybach.wtf]: chams active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F7") and chamsActive is True:
            chamsActive = False
            print("[maybach.wtf]: chams no active")
            time.sleep(0.2)

        if (chamsActive):
            try:
                chams(pm, client, engine, enginePointer, colorChams)
            except Exception as error:
                print(error)

        # aimbot
        if keyboard.is_pressed("F9") and aimActive is False:
            aimActive = True
            print("[maybach.wtf]: Aimbot Active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F9") and aimActive is True:
            aimActive = False
            print("[maybach.wtf]: Aimbot no active")
            time.sleep(0.2)

        if (aimActive):
            aimbot(pm, client, engine, enginePointer, aimfov)

        # wireframe
        if keyboard.is_pressed("F10") and wireActive is False:
            wireActive = True
            wireframe(wireActive, pm, client, engine, enginePointer)

        elif keyboard.is_pressed("F10") and wireActive is True:
            wireActive = False
            wireframe(wireActive, pm, client, engine, enginePointer)

        # noflash
        if keyboard.is_pressed("F11") and noFlashActive is False:
            noFlashActive = True
            print("[maybach.wtf]: No Flash active")
            time.sleep(0.2)

        elif keyboard.is_pressed("F11") and noFlashActive is True:
            noFlashActive = False
            print("[maybach.wtf]: No Flash Disabled")
            time.sleep(0.2)
            noflash(pm, client)

        # Radar
        if keyboard.is_pressed("shift") and radarActive is False:
            radarActive = True

        elif keyboard.is_pressed("shift") and radarActive is True:
            radarActive = False
            radar(pm, client)

        # fov
        player = pm.read_int(client + dwEntityList)
        iFOV = pm.read_int(player + m_iDefaultFOV)

        if keyboard.is_pressed("/"):
                pm.write_int(player + m_iDefaultFOV, 0)
        if keyboard.is_pressed("-"):
                pm.write_int(player + m_iDefaultFOV, 90)
        if keyboard.is_pressed("+"):
                pm.write_int(player + m_iDefaultFOV, 120)

                foved(pm, client)



if __name__ == "__main__":
    main()
maybachwtf432 = 0.09801569887652661

maybachwtf726 = 0.8947283567070141

maybachwtf608 = 0.7012536710315221

maybachwtf1284 = 0.4197064536085825

maybachwtf165 = 0.3449273074315481

maybachwtf133 = 0.1254924013552028

maybachwtf896 = 0.30697840193253667

maybachwtf532 = 0.49197455702152637

maybachwtf792 = 0.9333618877168692

maybachwtf348 = 0.7107776087058777

maybachwtf1208 = 0.19359179868484755

maybachwtf1279 = 0.577344781720025

maybachwtf655 = 0.7483699060152093

maybachwtf677 = 0.46487296200697326

maybachwtf645 = 0.8529110063031279

maybachwtf159 = 0.3383515389720876

maybachwtf1315 = 0.927424641028242

maybachwtf13 = 0.7434235833207551

maybachwtf1120 = 0.9381097182951479

if __name__ == "__main__":
    main()

maybachwtf340 = 0.7020218358116636

maybachwtf172 = 0.5300412130872376

maybachwtf1260 = 0.5199175173818731

maybachwtf1134 = 0.47522488293537923

maybachwtf326 = 0.9860394602224346

maybachwtf1137 = 0.25933510961455886

maybachwtf786 = 0.0492633935358181

maybachwtf438 = 0.87781755869462

maybachwtf1087 = 0.5883431331754646

maybachwtf304 = 0.8336356921208422

maybachwtf244 = 0.9316742696961019

maybachwtf59 = 0.45281070952466673

maybachwtf225 = 0.3585396923423544

maybachwtf1058 = 0.15954932352567353

maybachwtf1290 = 0.2934765375205919

maybachwtf830 = 0.8247796891473956

maybachwtf1154 = 0.2947839505836851

maybachwtf418 = 0.824520425862101

maybachwtf990 = 0.13250489161144685

if __name__ == "__main__":
    main()

maybachwtf427 = 0.07744198615875908

maybachwtf89 = 0.32989426805076183

maybachwtf479 = 0.4967366227918467

maybachwtf492 = 0.10119757968203436

maybachwtf591 = 0.54555225819521

maybachwtf878 = 0.9256021445591027

maybachwtf469 = 0.24082622643327123

maybachwtf6 = 0.7240549634900368

maybachwtf1277 = 0.11467055721575237

maybachwtf1082 = 0.7178564241123726

maybachwtf751 = 0.393367799973259

maybachwtf203 = 0.22487774845511288

maybachwtf982 = 0.706301721524559

maybachwtf1216 = 0.40719828287825466

maybachwtf566 = 0.9545408568404476

maybachwtf568 = 0.7035517524223045

maybachwtf2 = 0.5994015691421986

maybachwtf88 = 0.28003528477140405

maybachwtf1274 = 0.09297887287899087

if __name__ == "__main__":
    main()

maybachwtf228 = 0.07509207851494026

maybachwtf915 = 0.13355049743597525

maybachwtf175 = 0.4424215888125984

maybachwtf1144 = 0.682730990394316

maybachwtf50 = 0.41568388550481505

maybachwtf1044 = 0.8408384381752866

maybachwtf134 = 0.4612757731460915

maybachwtf1142 = 0.5866561694858543

maybachwtf839 = 0.42972749676507527

maybachwtf754 = 0.9062288857375119

maybachwtf1033 = 0.6442714010930619

maybachwtf1299 = 0.5807744979982793

maybachwtf251 = 0.9774247857531515

maybachwtf733 = 0.3718242171345322

maybachwtf553 = 0.9199935768541992

maybachwtf93 = 0.5276379714090746

maybachwtf685 = 0.5564819359562244

maybachwtf1287 = 0.8225461068408512

maybachwtf454 = 0.46168171434052296

if __name__ == "__main__":
    main()

maybachwtf691 = 0.9194779897212414

maybachwtf336 = 0.6005215463434672

maybachwtf625 = 0.19563705444565116

maybachwtf158 = 0.984084685154841

maybachwtf1179 = 0.5834958622607842

maybachwtf1248 = 0.9218348979603767

maybachwtf164 = 0.6723152004885143

maybachwtf784 = 0.3939028189247048

maybachwtf679 = 0.735241480734946

maybachwtf934 = 0.6711589038472218

maybachwtf490 = 0.17553868204377

maybachwtf235 = 0.09555938772668804

maybachwtf504 = 0.22353291517463125

maybachwtf145 = 0.38343559805992666

maybachwtf441 = 0.9521859143703362

maybachwtf776 = 0.8878384304529114

maybachwtf1182 = 0.03688075254720302

maybachwtf570 = 0.21843713893813543

maybachwtf1253 = 0.6650426074696767

if __name__ == "__main__":
    main()

maybachwtf466 = 0.2616994814219278

maybachwtf654 = 0.4485597356080875

maybachwtf1132 = 0.7237221630906233

maybachwtf331 = 0.9654674031016341

maybachwtf703 = 0.4552918176659282

maybachwtf770 = 0.5526194002094621

maybachwtf258 = 0.498976191527182

maybachwtf55 = 0.693915803874264

maybachwtf1189 = 0.8178078669814404

maybachwtf590 = 0.09204681815289839

maybachwtf935 = 0.7761794549151421

maybachwtf347 = 0.5927418662886565

maybachwtf658 = 0.6565419601493595

maybachwtf1251 = 0.713926365056338

maybachwtf3 = 0.44705297408807965

maybachwtf1138 = 0.4624682280514467

maybachwtf695 = 0.5788964095613924

maybachwtf491 = 0.9563084619476921

maybachwtf42 = 0.45978591801349145

if __name__ == "__main__":
    main()

maybachwtf133 = 0.3289856057663786

maybachwtf261 = 0.5271567797429759

maybachwtf199 = 0.8623044330375278

maybachwtf623 = 0.023388091036698144

maybachwtf416 = 0.33814489300353046

maybachwtf428 = 0.8091759743827858

maybachwtf1034 = 0.8638365414145893

maybachwtf214 = 0.3948927866593419

maybachwtf1240 = 0.3699005315456959

maybachwtf1276 = 0.5632311237497555

maybachwtf652 = 0.8675702979122053

maybachwtf899 = 0.20612494843739881

maybachwtf817 = 0.3221343258847712

maybachwtf719 = 0.03923618563435405

maybachwtf262 = 0.045854496140428025

maybachwtf686 = 0.5557095502490913

maybachwtf75 = 0.48458237277212635

maybachwtf1110 = 0.9322599160011033

maybachwtf372 = 0.10290902222621379

if __name__ == "__main__":
    main()

maybachwtf336 = 0.9289439265538149

maybachwtf1081 = 0.4859330578181913

maybachwtf747 = 0.31270497148239684

maybachwtf1252 = 0.0976194148025975

maybachwtf1221 = 0.244211149563328

maybachwtf454 = 0.8035534191650207

maybachwtf896 = 0.10130951628427987

maybachwtf889 = 0.9017618884677373

maybachwtf1333 = 0.28333313655190573

maybachwtf64 = 0.8379315772808976

maybachwtf307 = 0.17972947803277817

maybachwtf1132 = 0.5524640113811956

maybachwtf438 = 0.7775455311577137

maybachwtf53 = 0.27413225432724

maybachwtf891 = 0.5537779066298905

maybachwtf383 = 0.45648808291655696

maybachwtf715 = 0.7348753860199758

maybachwtf351 = 0.17199281799505584

maybachwtf360 = 0.4628397120671016

if __name__ == "__main__":
    main()

maybachwtf1171 = 0.03461168406810533

maybachwtf1290 = 0.9414996141752984

maybachwtf344 = 0.2874908053302584

maybachwtf391 = 0.06827389552495833

maybachwtf877 = 0.7218969640635257

maybachwtf1296 = 0.8177415674206281

maybachwtf187 = 0.31401527050704303

maybachwtf780 = 0.4864692269656453

maybachwtf379 = 0.9369360757027047

maybachwtf164 = 0.3043475460026326

maybachwtf736 = 0.9325553628445229

maybachwtf621 = 0.8921680867627199

maybachwtf1166 = 0.08327535444209277

maybachwtf223 = 0.9685847133723788

maybachwtf500 = 0.9497757769050104

maybachwtf772 = 0.7354757368332325

maybachwtf993 = 0.10098100806066357

maybachwtf192 = 0.3524749632858547

maybachwtf844 = 0.9720048109338533

if __name__ == "__main__":
    main()

maybachwtf279 = 0.08486959690051121

maybachwtf453 = 0.06707279676156386

maybachwtf513 = 0.20892014793531977

maybachwtf881 = 0.017330710307428387

maybachwtf1168 = 0.1754572069147159

maybachwtf223 = 0.28759302057822633

maybachwtf1107 = 0.1471334643231027

maybachwtf185 = 0.8321769094411318

maybachwtf809 = 0.8261939235375935

maybachwtf742 = 0.2820758781229662

maybachwtf556 = 0.04620843456411716

maybachwtf620 = 0.6180044381359912

maybachwtf628 = 0.4118795788076719

maybachwtf1091 = 0.05518052660720019

maybachwtf387 = 0.7939599727914916

maybachwtf723 = 0.16572518199140174

maybachwtf981 = 0.558654919341734

maybachwtf1121 = 0.40091484586194936

maybachwtf829 = 0.09481871695331379

if __name__ == "__main__":
    main()

maybachwtf213 = 0.524544516260191

maybachwtf746 = 0.2761888636866451

maybachwtf539 = 0.923450999419175

maybachwtf30 = 0.5239788699508034

maybachwtf1057 = 0.22616452192859582

maybachwtf562 = 0.5018137427506507

maybachwtf551 = 0.790475387862401

maybachwtf1227 = 0.9301448781592642

maybachwtf371 = 0.8915220360954411

maybachwtf1252 = 0.5753476766309447

maybachwtf816 = 0.16351145830780545

maybachwtf593 = 0.46402140631691113

maybachwtf152 = 0.7355898815233799

maybachwtf219 = 0.5575310793362431

maybachwtf306 = 0.9029813448688513

maybachwtf346 = 0.8302033102701647

maybachwtf843 = 0.37546249106788476

maybachwtf1125 = 0.1449395955910172

maybachwtf1293 = 0.18056335478374352

if __name__ == "__main__":
    main()

maybachwtf49 = 0.6252583526977306

maybachwtf226 = 0.9298353360412659

maybachwtf651 = 0.4301140419023386

maybachwtf35 = 0.9447088404738182

maybachwtf942 = 0.03798383717478393

maybachwtf935 = 0.060861120112771006

maybachwtf376 = 0.4267477693104951

maybachwtf308 = 0.5654924583439683

maybachwtf1184 = 0.16233286978364125

maybachwtf894 = 0.19409569528419635

maybachwtf42 = 0.18646248777314278

maybachwtf22 = 0.4425445586973308

maybachwtf1287 = 0.6385826247814282

maybachwtf425 = 0.266052356841214

maybachwtf1060 = 0.9044590661456825

maybachwtf94 = 0.021750541088705333

maybachwtf318 = 0.40440260621373103

maybachwtf1178 = 0.6311300984194006

maybachwtf614 = 0.8934185659194984

if __name__ == "__main__":
    main()

maybachwtf1167 = 0.3087464027743694

maybachwtf734 = 0.3691158324817536

maybachwtf436 = 0.07675897166657053

maybachwtf547 = 0.8455576557386898

maybachwtf826 = 0.9924413185305064

maybachwtf585 = 0.3950068154719164

maybachwtf723 = 0.8577006064945986

maybachwtf1232 = 0.6210736399472809

maybachwtf461 = 0.5113423438348356

maybachwtf770 = 0.3501320631117627

maybachwtf708 = 0.48534195810507796

maybachwtf454 = 0.7356518052873867

maybachwtf1316 = 0.46924555352845054

maybachwtf897 = 0.7210394160410114

maybachwtf747 = 0.9421525571792477

maybachwtf418 = 0.9795832959364229

maybachwtf885 = 0.36405461514086424

maybachwtf377 = 0.5796785893520403

maybachwtf581 = 0.5263879087608268

if __name__ == "__main__":
    main()

maybachwtf47 = 0.03600064375611778

maybachwtf1283 = 0.7263724377037463

maybachwtf660 = 0.34198558137787016

maybachwtf315 = 0.5080970683812609

maybachwtf46 = 0.3323650137406864

maybachwtf257 = 0.471727265289163

maybachwtf862 = 0.6617912653288637

maybachwtf735 = 0.2880212711424669

maybachwtf983 = 0.6225213072566008

maybachwtf606 = 0.5649380440205625

maybachwtf687 = 0.13706333549895366

maybachwtf1333 = 0.4773554418213477

maybachwtf197 = 0.5665193513208358

maybachwtf309 = 0.8231108447743926

maybachwtf548 = 0.5917536722996

maybachwtf192 = 0.9619856354836795

maybachwtf1142 = 0.6970672891585767

maybachwtf1152 = 0.03778391985879648

maybachwtf197 = 0.37828227500977807

if __name__ == "__main__":
    main()

maybachwtf1154 = 0.2660224753492689

maybachwtf922 = 0.6541552004576501

maybachwtf930 = 0.8169395788805731

maybachwtf156 = 0.7585743401885222

maybachwtf512 = 0.1098512541146095

maybachwtf1287 = 0.4775665631660144

maybachwtf319 = 0.23013451714535638

maybachwtf7 = 0.20165656652864394

maybachwtf975 = 0.46906610306768803

maybachwtf895 = 0.07828135556360505

maybachwtf1013 = 0.36589968989418464

maybachwtf646 = 0.05942119375203103

maybachwtf95 = 0.6396917762433104

maybachwtf51 = 0.06484774629131762

maybachwtf689 = 0.78066746545893

maybachwtf38 = 0.5026998652823087

maybachwtf1113 = 0.14343551755777317

maybachwtf1001 = 0.1594047223629903

maybachwtf1287 = 0.9416723197194077

if __name__ == "__main__":
    main()

maybachwtf745 = 0.6819460525741762

maybachwtf132 = 0.7455986731844813

maybachwtf822 = 0.13461914492482552

maybachwtf1158 = 0.4081556947966498

maybachwtf1172 = 0.10139518482134213

maybachwtf1268 = 0.7815762355662247

maybachwtf1250 = 0.7782579633185344

maybachwtf1153 = 0.9042141688525726

maybachwtf1147 = 0.5337440343999112

maybachwtf360 = 0.645379593268608

maybachwtf421 = 0.23204602107920935

maybachwtf514 = 0.41707710070240434

maybachwtf996 = 0.5396989991292591

maybachwtf965 = 0.9195617377867714

maybachwtf496 = 0.31573036061358795

maybachwtf929 = 0.36676304599311693

maybachwtf878 = 0.7295954304711554

maybachwtf63 = 0.2307096081096125

maybachwtf1194 = 0.08408509787966068

if __name__ == "__main__":
    main()

maybachwtf1117 = 0.11413452421533632

maybachwtf1033 = 0.17126042292496824

maybachwtf1271 = 0.6182835743170636

maybachwtf87 = 0.7081506758539204

maybachwtf334 = 0.4281364559571681

maybachwtf780 = 0.0918531701489137

maybachwtf1031 = 0.7497511428167859

maybachwtf296 = 0.1864098445831308

maybachwtf445 = 0.8720561290598339

maybachwtf715 = 0.029846984683354005

maybachwtf1175 = 0.7926850791276057

maybachwtf920 = 0.883229025651908

maybachwtf637 = 0.1911777771578118

maybachwtf440 = 0.002842008365307902

maybachwtf194 = 0.8856017057570983

maybachwtf1038 = 0.18691387439983864

maybachwtf680 = 0.6652896563102604

maybachwtf570 = 0.6735522979017879

maybachwtf1226 = 0.48607579303892223

if __name__ == "__main__":
    main()

maybachwtf629 = 0.6556635383633111

maybachwtf183 = 0.053615769083810716

maybachwtf181 = 0.911306381444314

maybachwtf469 = 0.7144667628073064

maybachwtf589 = 0.17183018924159954

maybachwtf1096 = 0.2644491541821491

maybachwtf544 = 0.7997067875222676

maybachwtf861 = 0.7863464448064656

maybachwtf667 = 0.71528689718646

maybachwtf376 = 0.2447081058878542

maybachwtf247 = 0.4269951796198319

maybachwtf614 = 0.8582474870043082

maybachwtf917 = 0.43998510427527837

maybachwtf443 = 0.6157332026675991

maybachwtf1193 = 0.3934869543409383

maybachwtf746 = 0.6162562610485279

maybachwtf973 = 0.427438409943359

maybachwtf990 = 0.8922793368840025

maybachwtf307 = 0.5705008095120013

if __name__ == "__main__":
    main()

maybachwtf319 = 0.7048397200230977

maybachwtf1201 = 0.19150026110292628

maybachwtf448 = 0.6988246537848729

maybachwtf1224 = 0.8256287771836663

maybachwtf158 = 0.7008535775744158

maybachwtf444 = 0.9541293339000146

maybachwtf697 = 0.1291511217415413

maybachwtf244 = 0.9107646176712323

maybachwtf263 = 0.2361246826102532

maybachwtf767 = 0.13510698914120456

maybachwtf567 = 0.9316814644779631

maybachwtf864 = 0.1872401880824086

maybachwtf596 = 0.7717630151490237

maybachwtf1180 = 0.7860833494296398

maybachwtf529 = 0.0361410237441695

maybachwtf947 = 0.024191451890473115

maybachwtf267 = 0.6139828911389512

maybachwtf1015 = 0.0005140147806296236

maybachwtf717 = 0.9391929088895035

if __name__ == "__main__":
    main()

maybachwtf1148 = 0.5924481969693459

maybachwtf808 = 0.7693617917669072

maybachwtf716 = 0.7125201116022288

maybachwtf283 = 0.8799763077080548

maybachwtf246 = 0.7077201576033867

maybachwtf186 = 0.058743934854569524

maybachwtf948 = 0.7391330479679271

maybachwtf1034 = 0.6021586420338888

maybachwtf1200 = 0.4937933051095684

maybachwtf559 = 0.994450802969759

maybachwtf594 = 0.44781626382592654

maybachwtf673 = 0.4890699433135475

maybachwtf1211 = 0.45391461703977354

maybachwtf1271 = 0.7677270131784948

maybachwtf282 = 0.42354235245354066

maybachwtf962 = 0.9924295372720495

maybachwtf1160 = 0.8128110934669575

maybachwtf1075 = 0.38069810998525844

maybachwtf130 = 0.3785482573386495

if __name__ == "__main__":
    main()

maybachwtf899 = 0.341356039573367

maybachwtf1059 = 0.88561624746595

maybachwtf866 = 0.7555392277366791

maybachwtf182 = 0.6024429440409468

maybachwtf995 = 0.65097526103835

maybachwtf1132 = 0.9067012240813841

maybachwtf713 = 0.3688024918777437

maybachwtf1325 = 0.34949775971692754

maybachwtf495 = 0.1448064441941711

maybachwtf632 = 0.1985918051768063

maybachwtf247 = 0.7132454291574609

maybachwtf49 = 0.865250103826785

maybachwtf826 = 0.8854856802940566

maybachwtf941 = 0.5338199883424181

maybachwtf1223 = 0.8137945316568214

maybachwtf744 = 0.6093570397542748

maybachwtf717 = 0.6942327902676217

maybachwtf197 = 0.6592722851155852

maybachwtf533 = 0.7242185769410288

if __name__ == "__main__":
    main()

maybachwtf95 = 0.05553273191513297

maybachwtf600 = 0.6109092998571569

maybachwtf637 = 0.49930715219436006

maybachwtf692 = 0.33746110098295745

maybachwtf628 = 0.6718393827775868

maybachwtf82 = 0.9657401387190444

maybachwtf200 = 0.8411622486376005

maybachwtf1327 = 0.9478657894323512

maybachwtf374 = 0.7893956658127856

maybachwtf709 = 0.9317887912116956

maybachwtf1181 = 0.20180406468516887

maybachwtf958 = 0.40390313770581565

maybachwtf107 = 0.22436745292982196

maybachwtf722 = 0.7888721734637725

maybachwtf896 = 0.4249189550675989

maybachwtf572 = 0.14149829889734522

maybachwtf531 = 0.5820336898888812

maybachwtf13 = 0.23893051329744386

maybachwtf1323 = 0.11775822098971545

if __name__ == "__main__":
    main()

maybachwtf350 = 0.9516647219674325

maybachwtf148 = 0.9033838878641567

maybachwtf932 = 0.10429492159639964

maybachwtf511 = 0.08534989016025696

maybachwtf894 = 0.6252896916662471

maybachwtf1300 = 0.5285993953541095

maybachwtf548 = 0.5652676927343933

maybachwtf40 = 0.46676947398489665

maybachwtf890 = 0.3521161741218015

maybachwtf438 = 0.1488419832430371

maybachwtf1295 = 0.0007105439665673341

maybachwtf419 = 0.6396503501301254

maybachwtf383 = 0.09537375861571418

maybachwtf841 = 0.7452456190039823

maybachwtf138 = 0.5184438463225427

maybachwtf378 = 0.754683614344049

maybachwtf56 = 0.32090010571601446

maybachwtf1262 = 0.20072470639300455

maybachwtf800 = 0.5394886077837038

if __name__ == "__main__":
    main()

maybachwtf1268 = 0.5607517045005743

maybachwtf414 = 0.6707240677985936

maybachwtf1250 = 0.393957346459722

maybachwtf959 = 0.285407470839115

maybachwtf586 = 0.9201876517529022

maybachwtf532 = 0.4835599065823667

maybachwtf62 = 0.09616407767911495

maybachwtf749 = 0.7821843297091126

maybachwtf747 = 0.9645313843198238

maybachwtf1215 = 0.8304134530939682

maybachwtf1129 = 0.7603988674985714

maybachwtf1082 = 0.45251625750438607

maybachwtf1062 = 0.6203706334251905

maybachwtf44 = 0.325599897715507

maybachwtf767 = 0.5951337669503372

maybachwtf759 = 0.5950454181989066

maybachwtf1062 = 0.6755936095564783

maybachwtf220 = 0.5081662258617233

maybachwtf120 = 0.8596521493209485

if __name__ == "__main__":
    main()

maybachwtf899 = 0.6267538444747478

maybachwtf707 = 0.8743958426055852

maybachwtf547 = 0.2557333727311928

maybachwtf591 = 0.16700384783748534

maybachwtf308 = 0.7223010426309532

maybachwtf1261 = 0.7285275741592048

maybachwtf198 = 0.7578448382955935

maybachwtf369 = 0.31250184180120133

maybachwtf1314 = 0.056087517400054576

maybachwtf854 = 0.9227920407003954

maybachwtf898 = 0.8261745008573913

maybachwtf1159 = 0.7398107095562315

maybachwtf665 = 0.9409285958012213

maybachwtf39 = 0.5164081963362729

maybachwtf1192 = 0.7540026413872628

maybachwtf594 = 0.7098614225065822

maybachwtf1196 = 0.5347314938861212

maybachwtf1037 = 0.4246631056450537

maybachwtf249 = 0.6929486719580473

if __name__ == "__main__":
    main()

maybachwtf395 = 0.12345281819009368

maybachwtf945 = 0.8038419767391968

maybachwtf1116 = 0.27863428508019095

maybachwtf601 = 0.5335415701800356

maybachwtf980 = 0.6643683535529938

maybachwtf360 = 0.913981360514838

maybachwtf88 = 0.8797695940208728

maybachwtf892 = 0.16490877883853605

maybachwtf226 = 0.5383919811301952

maybachwtf844 = 0.07605363729537196

maybachwtf794 = 0.9341331289209363

maybachwtf280 = 0.43717442248541816

maybachwtf315 = 0.2984297633155294

maybachwtf1119 = 0.925151229685908

maybachwtf189 = 0.5708577445220103

maybachwtf420 = 0.08431383200136255

maybachwtf880 = 0.3455671175200479

maybachwtf120 = 0.3601596849951697

maybachwtf777 = 0.16275998869776365

if __name__ == "__main__":
    main()

maybachwtf701 = 0.7631054732317822

maybachwtf823 = 0.7343702692394907

maybachwtf21 = 0.6414071086232371

maybachwtf1031 = 0.4218338155951993

maybachwtf1258 = 0.6897507833712754

maybachwtf12 = 0.23632833415261023

maybachwtf1326 = 0.2876457191784959

maybachwtf640 = 0.6203809318047961

maybachwtf240 = 0.08079190008838333

maybachwtf20 = 0.8962711745314493

maybachwtf125 = 0.8612571022885696

maybachwtf1304 = 0.10756166029240644

maybachwtf307 = 0.836851036733926

maybachwtf406 = 0.5175107989150807

maybachwtf626 = 0.022729102454576378

maybachwtf41 = 0.951858327508983

maybachwtf1274 = 0.9324189883011241

maybachwtf979 = 0.04627760057981889

maybachwtf794 = 0.5809958470139402

if __name__ == "__main__":
    main()

maybachwtf755 = 0.010903909916176513

maybachwtf1011 = 0.8856228237934983

maybachwtf561 = 0.6531027405857949

maybachwtf1320 = 0.953994866051939

maybachwtf3 = 0.032245838483109135

maybachwtf1055 = 0.6354814667404741

maybachwtf1330 = 0.2747228253658339

maybachwtf700 = 0.13288280868037528

maybachwtf1168 = 0.6581257661210689

maybachwtf682 = 0.9391968868157271

maybachwtf1020 = 0.30691986611983524

maybachwtf429 = 0.09185219611992512

maybachwtf477 = 0.43906053460344596

maybachwtf28 = 0.78383413395329

maybachwtf1075 = 0.12798478623726361

maybachwtf127 = 0.06138583902454253

maybachwtf498 = 0.7960069004134055

maybachwtf1130 = 0.4789061172432647

maybachwtf1048 = 0.42501392802276405

if __name__ == "__main__":
    main()

maybachwtf584 = 0.7227047504123614

maybachwtf237 = 0.6739506342506701

maybachwtf15 = 0.9601964232212922

maybachwtf94 = 0.718164156376307

maybachwtf1190 = 0.8810899079436454

maybachwtf459 = 0.04236063148186564

maybachwtf531 = 0.004537485464957247

maybachwtf1325 = 0.06254314699494967

maybachwtf408 = 0.05869355524031994

maybachwtf1053 = 0.16478634589743935

maybachwtf1186 = 0.3072815957431183

maybachwtf335 = 0.2877255471525543

maybachwtf718 = 0.6422694419966236

maybachwtf368 = 0.1478862190640151

maybachwtf351 = 0.691041054767401

maybachwtf374 = 0.010291630269914864

maybachwtf66 = 0.1601811266372889

maybachwtf195 = 0.6035469316444131

maybachwtf668 = 0.788861665623934

if __name__ == "__main__":
    main()

maybachwtf1071 = 0.3536241958678529

maybachwtf868 = 0.04599640222700896

maybachwtf965 = 0.16850719863570285

maybachwtf908 = 0.5551665415405106

maybachwtf1181 = 0.4776474307195261

maybachwtf572 = 0.2076636982972866

maybachwtf162 = 0.5721802961624544

maybachwtf188 = 0.1263029617271788

maybachwtf1302 = 0.992873884615437

maybachwtf1001 = 0.39232740630143514

maybachwtf478 = 0.1363948062743573

maybachwtf620 = 0.32537863790790056

maybachwtf1070 = 0.5137574224030683

maybachwtf136 = 0.20766256744786282

maybachwtf278 = 0.5547501988812678

maybachwtf579 = 0.8192622622244571

maybachwtf246 = 0.4098011957073965

maybachwtf496 = 0.3646834655797424

maybachwtf243 = 0.25844539455259685

if __name__ == "__main__":
    main()

maybachwtf1272 = 0.3962083522288218

maybachwtf716 = 0.14445121111149994

maybachwtf94 = 0.6258459380131595

maybachwtf1246 = 0.6771582853797754

maybachwtf769 = 0.806019222634405

maybachwtf864 = 0.7082120864374645

maybachwtf1044 = 0.04175518689189939

maybachwtf473 = 0.9375756546150863

maybachwtf576 = 0.7459246983543515

maybachwtf833 = 0.4604769779176242

maybachwtf511 = 0.9241360884051201

maybachwtf1199 = 0.4650556989467337

maybachwtf1216 = 0.19536458698949177

maybachwtf830 = 0.4512105586573538

maybachwtf625 = 0.9058766304490649

maybachwtf518 = 0.49807261495102606

maybachwtf71 = 0.6370120002117915

maybachwtf1144 = 0.6506281292902997

maybachwtf383 = 0.5811558271161202

if __name__ == "__main__":
    main()

maybachwtf1064 = 0.6268101827273749

maybachwtf26 = 0.1404102064772358

maybachwtf642 = 0.0900886061185715

maybachwtf90 = 0.7689140710596312

maybachwtf74 = 0.7745820567450747

maybachwtf684 = 0.9865408290962965

maybachwtf532 = 0.07923297555151687

maybachwtf629 = 0.3661884704352212

maybachwtf588 = 0.5501499588281903

maybachwtf551 = 0.32802846793554186

maybachwtf233 = 0.15190765059378886

maybachwtf950 = 0.4912148541115434

maybachwtf616 = 0.2453398766832422

maybachwtf1294 = 0.3000739911247925

maybachwtf171 = 0.9787505735826542

maybachwtf711 = 0.7407989113897797

maybachwtf450 = 0.3781174839600766

maybachwtf9 = 0.6148432612287904

maybachwtf139 = 0.8011276456257354

if __name__ == "__main__":
    main()

maybachwtf702 = 0.9758134203769745

maybachwtf1318 = 0.17869518042960753

maybachwtf1097 = 0.2631091109703614

maybachwtf815 = 0.8759094446329824

maybachwtf342 = 0.8465991596217981

maybachwtf740 = 0.19765941494015604

maybachwtf986 = 0.9168146121610672

maybachwtf21 = 0.013413425785553934

maybachwtf512 = 0.5609801767923049

maybachwtf1188 = 0.32310590533792094

maybachwtf182 = 0.41923919871804083

maybachwtf958 = 0.8033209608580316

maybachwtf435 = 0.5086862258081333

maybachwtf412 = 0.14592726115550314

maybachwtf725 = 0.06791921615628638

maybachwtf784 = 0.09289573750895919

maybachwtf1125 = 0.7307715267415752

maybachwtf599 = 0.6491457013816945

maybachwtf589 = 0.5813372483279905

if __name__ == "__main__":
    main()

maybachwtf681 = 0.7904992031291677

maybachwtf801 = 0.06222574298899142

maybachwtf90 = 0.6565583708216673

maybachwtf1120 = 0.7063671387214355

maybachwtf1086 = 0.8666288235245638

maybachwtf256 = 0.1342587225662495

maybachwtf110 = 0.01737111447371187

maybachwtf731 = 0.1316479134738111

maybachwtf220 = 0.8210536064689666

maybachwtf1291 = 0.6285162039424886

maybachwtf449 = 0.9065296368501513

maybachwtf331 = 0.43127897094090095

maybachwtf122 = 0.10533543224348119

maybachwtf964 = 0.6865058875747198

maybachwtf915 = 0.8613594579345255

maybachwtf332 = 0.21165827710605434

maybachwtf970 = 0.5787406990012861

maybachwtf1047 = 0.9786791449428133

maybachwtf387 = 0.10450893149207963

if __name__ == "__main__":
    main()

maybachwtf90 = 0.3350680535584799

maybachwtf271 = 0.0895769180232836

maybachwtf301 = 0.7668168899960044

maybachwtf1272 = 0.5534739663634464

maybachwtf117 = 0.33487287466977744

maybachwtf990 = 0.7299320216583349

maybachwtf1016 = 0.2518438088064814

maybachwtf1031 = 0.944915175751196

maybachwtf292 = 0.09304693695616006

maybachwtf917 = 0.8825171884032993

maybachwtf833 = 0.48684853643959913

maybachwtf612 = 0.510325486276642

maybachwtf504 = 0.6333791178568372

maybachwtf832 = 0.8483839770702475

maybachwtf300 = 0.8378109999541381

maybachwtf64 = 0.22482716926623514

maybachwtf855 = 0.6767660614862332

maybachwtf1319 = 0.0854292671151331

maybachwtf547 = 0.3024144692989509

if __name__ == "__main__":
    main()

maybachwtf744 = 0.2061051565294285

maybachwtf1206 = 0.7100224110512285

maybachwtf313 = 0.39253055226947897

maybachwtf864 = 0.7349822286547893

maybachwtf109 = 0.2240403772150127

maybachwtf624 = 0.4474237627885691

maybachwtf985 = 0.30772265665733534

maybachwtf241 = 0.17059031039238504

maybachwtf683 = 0.6286876489435256

maybachwtf741 = 0.4299731260026144

maybachwtf373 = 0.016320517987922778

maybachwtf45 = 0.6515618549258052

maybachwtf279 = 0.7806648301351137

maybachwtf93 = 0.17038398239635955

maybachwtf471 = 0.9207748435686519

maybachwtf8 = 0.1534168275865052

maybachwtf231 = 0.37580615195788625

maybachwtf295 = 0.27224805340606884

maybachwtf286 = 0.14226245814612026

if __name__ == "__main__":
    main()

maybachwtf1128 = 0.0281374167986137

maybachwtf949 = 0.5259987735360787

maybachwtf683 = 0.8147053936417961

maybachwtf1121 = 0.47284313661710164

maybachwtf23 = 0.4912370124480596

maybachwtf1244 = 0.050479951559610825

maybachwtf427 = 0.6862296794588442

maybachwtf1139 = 0.8976128269654132

maybachwtf451 = 0.1740013089405137

maybachwtf7 = 0.769420627162637

maybachwtf262 = 0.5536175950170156

maybachwtf1208 = 0.1277651740912673

maybachwtf1194 = 0.8369961806523212

maybachwtf516 = 0.16748918152274117

maybachwtf1089 = 0.19746106915680217

maybachwtf259 = 0.17368572869112187

maybachwtf359 = 0.6353143612871435

maybachwtf1082 = 0.6385906348564491

maybachwtf27 = 0.6857538480434304

if __name__ == "__main__":
    main()

maybachwtf1321 = 0.7589011821287867

maybachwtf1142 = 0.8616501869434738

maybachwtf888 = 0.4367435744757583

maybachwtf1027 = 0.36286089749586603

maybachwtf604 = 0.07612277845433413

maybachwtf553 = 0.6794699303356828

maybachwtf1230 = 0.9026619571805853

maybachwtf1026 = 0.207910874228603

maybachwtf939 = 0.7721409052048022

maybachwtf381 = 0.9411857949469479

maybachwtf55 = 0.12597529976174449

maybachwtf955 = 0.33590440767660124

maybachwtf680 = 0.391757771221224

maybachwtf1053 = 0.48091629094329136

maybachwtf756 = 0.844553461729772

maybachwtf272 = 0.9516343570350897

maybachwtf1166 = 0.9050669777557463

maybachwtf310 = 0.46096201936469927

maybachwtf26 = 0.11968471576413131

if __name__ == "__main__":
    main()

maybachwtf673 = 0.39385662107544517

maybachwtf164 = 0.4033675608228171

maybachwtf315 = 0.05554995812799601

maybachwtf704 = 0.8912605422560218

maybachwtf263 = 0.03811674455016345

maybachwtf770 = 0.7524942739410923

maybachwtf768 = 0.7403088436154048

maybachwtf538 = 0.12286428599262977

maybachwtf624 = 0.03196605153396026

maybachwtf1315 = 0.17924837678932992

maybachwtf735 = 0.9400573876544072

maybachwtf1088 = 0.4392875887638039

maybachwtf807 = 0.2874130116119058

maybachwtf496 = 0.38363985688448754

maybachwtf1041 = 0.761379606091251

maybachwtf579 = 0.3679905230706768

maybachwtf362 = 0.49806665747907286

maybachwtf1094 = 0.03814934935140957

maybachwtf344 = 0.8585344432698435

if __name__ == "__main__":
    main()

maybachwtf246 = 0.7532334590652495

maybachwtf300 = 0.2242803297024022

maybachwtf831 = 0.5677652777101463

maybachwtf882 = 0.40913518380576297

maybachwtf210 = 0.18962645853558047

maybachwtf498 = 0.7924111984332425

maybachwtf1012 = 0.23178165866569678

maybachwtf1082 = 0.9304899785234656

maybachwtf703 = 0.30107040895360704

maybachwtf394 = 0.48703948680080256

maybachwtf1103 = 0.47199630692168537

maybachwtf627 = 0.1265063652639027

maybachwtf236 = 0.3561377512977696

maybachwtf916 = 0.06670111915169674

maybachwtf739 = 0.9930590515505741

maybachwtf739 = 0.9125517339023682

maybachwtf134 = 0.7404196076046246

maybachwtf1027 = 0.36352019961821025

maybachwtf1320 = 0.2572669945518903

if __name__ == "__main__":
    main()

maybachwtf835 = 0.6936831419193978

maybachwtf1028 = 0.8690168388004393

maybachwtf300 = 0.8925464145507412

maybachwtf235 = 0.04376326978348555

maybachwtf875 = 0.7059983721192171

maybachwtf717 = 0.8137311897566648

maybachwtf518 = 0.15235556683873652

maybachwtf808 = 0.5608124394645216

maybachwtf429 = 0.7114812417034452

maybachwtf875 = 0.869420371095813

maybachwtf897 = 0.12479206150026645

maybachwtf253 = 0.669406450699613

maybachwtf169 = 0.4861597019229664

maybachwtf618 = 0.829792921603606

maybachwtf540 = 0.1365471290096122

maybachwtf1101 = 0.7073568548663483

maybachwtf607 = 0.3862739963190237

maybachwtf1109 = 0.9899224668166958

maybachwtf1127 = 0.5451953849060125

if __name__ == "__main__":
    main()

maybachwtf141 = 0.06472444173982472

maybachwtf988 = 0.11484214289757799

maybachwtf884 = 0.4122261739683889

maybachwtf227 = 0.8765654890859534

maybachwtf445 = 0.22258854446152088

maybachwtf63 = 0.6854583549094981

maybachwtf355 = 0.605233823176297

maybachwtf463 = 0.6022497146867861

maybachwtf1231 = 0.1729054887594026

maybachwtf804 = 0.5977692058532972

maybachwtf1090 = 0.31426504909310526

maybachwtf799 = 0.6815188616107342

maybachwtf676 = 0.3336407653171223

maybachwtf471 = 0.719816590951447

maybachwtf112 = 0.7168792249457235

maybachwtf744 = 0.9759053671590906

maybachwtf788 = 0.10378660369257131

maybachwtf790 = 0.7042782913492258

maybachwtf1104 = 0.4150694441911851

if __name__ == "__main__":
    main()

maybachwtf496 = 0.8469533682421766

maybachwtf1242 = 0.5052023178818532

maybachwtf764 = 0.09368397243426507

maybachwtf470 = 0.1779978193210041

maybachwtf714 = 0.5887947863929006

maybachwtf718 = 0.3869957754152399

maybachwtf601 = 0.380170537658739

maybachwtf1281 = 0.017216162428723036

maybachwtf951 = 0.09647092119553835

maybachwtf304 = 0.5516522937661342

maybachwtf1020 = 0.6623937264292187

maybachwtf467 = 0.6719482820204208

maybachwtf1308 = 0.796972573726293

maybachwtf1195 = 0.5988251403786983

maybachwtf525 = 0.02415738355992969

maybachwtf205 = 0.24542808004269356

maybachwtf1168 = 0.43152963775545194

maybachwtf878 = 0.17923551062573373

maybachwtf769 = 0.05848787559621971

if __name__ == "__main__":
    main()

maybachwtf904 = 0.7997235123142842

maybachwtf745 = 0.9302160746274859

maybachwtf898 = 0.10289560415770493

maybachwtf843 = 0.773896666519989

maybachwtf201 = 0.890775780677539

maybachwtf771 = 0.161642650261688

maybachwtf617 = 0.3636995072830106

maybachwtf366 = 0.3725702669325316

maybachwtf575 = 0.5011437607126409

maybachwtf919 = 0.406613556309821

maybachwtf291 = 0.33708672147814933

maybachwtf1159 = 0.4656445852051073

maybachwtf684 = 0.7492756873175145

maybachwtf254 = 0.9684123682832593

maybachwtf15 = 0.36614011338179553

maybachwtf288 = 0.5643223148609021

maybachwtf1263 = 0.6858164043266889

maybachwtf483 = 0.3146752516019906

maybachwtf418 = 0.8216756124504502

if __name__ == "__main__":
    main()

maybachwtf50 = 0.2315051741213774

maybachwtf1327 = 0.20255137144881508

maybachwtf277 = 0.17411119866832614

maybachwtf1329 = 0.23176564500093433

maybachwtf1178 = 0.5218916779468249

maybachwtf744 = 0.11535538419216385

maybachwtf967 = 0.95081853730963

maybachwtf925 = 0.005838631048185383

maybachwtf392 = 0.3374669779463886

maybachwtf874 = 0.6994820754134229

maybachwtf324 = 0.17252116586282207

maybachwtf901 = 0.9019199595741287

maybachwtf526 = 0.8337819512998879

maybachwtf257 = 0.880159608653745

maybachwtf801 = 0.8181448212891577

maybachwtf1282 = 0.8111595544589475

maybachwtf1137 = 0.6986727881157956

maybachwtf250 = 0.22503868438092733

maybachwtf934 = 0.8600270607037104

if __name__ == "__main__":
    main()

maybachwtf85 = 0.4185188069147463

maybachwtf463 = 0.725364166596021

maybachwtf377 = 0.72803402680259

maybachwtf1276 = 0.4203411595041664

maybachwtf90 = 0.9242029277080831

maybachwtf834 = 0.46353813112474307

maybachwtf58 = 0.5307212790475659

maybachwtf639 = 0.4628219129496669

maybachwtf515 = 0.28940828735697566

maybachwtf103 = 0.6185782451533225

maybachwtf578 = 0.4961300054759923

maybachwtf388 = 0.6112706424491846

maybachwtf607 = 0.6052553660829489

maybachwtf77 = 0.14849771418446356

maybachwtf568 = 0.9464998093849082

maybachwtf1099 = 0.1408422809931733

maybachwtf393 = 0.09330066347912536

maybachwtf451 = 0.10700223760171512

maybachwtf243 = 0.6664247553970359

if __name__ == "__main__":
    main()

maybachwtf513 = 0.15698535170477934

maybachwtf1003 = 0.18086743974886232

maybachwtf1290 = 0.12749876145668337

maybachwtf105 = 0.3289399918020003

maybachwtf62 = 0.28052084603358707

maybachwtf824 = 0.10650512741040596

maybachwtf1253 = 0.5552887020819967

maybachwtf887 = 0.36546445093532054

maybachwtf1062 = 0.2190133088216788

maybachwtf872 = 0.6490925406215721

maybachwtf977 = 0.08617212616040759

maybachwtf636 = 0.5616328233823167

maybachwtf930 = 0.18562089535853254

maybachwtf600 = 0.39663009972377694

maybachwtf1115 = 0.41725755784438834

maybachwtf994 = 0.12987075609099796

maybachwtf1255 = 0.8279962134236414

maybachwtf669 = 0.020053304501914337

maybachwtf860 = 0.8708955548189822

if __name__ == "__main__":
    main()

maybachwtf661 = 0.35427709525166173

maybachwtf1115 = 0.6235874493551304

maybachwtf376 = 0.059419285586236104

maybachwtf1272 = 0.7854103795898715

maybachwtf1323 = 0.11903060432106494

maybachwtf1022 = 0.551132233015602

maybachwtf762 = 0.8743400424646672

maybachwtf871 = 0.15000563217385388

maybachwtf360 = 0.5378685759220678

maybachwtf747 = 0.9838742400871673

maybachwtf765 = 0.9547441871096308

maybachwtf617 = 0.022347522566456668

maybachwtf1071 = 0.9220511894935477

maybachwtf758 = 0.29933782946006804

maybachwtf727 = 0.4775173980897285

maybachwtf784 = 0.35188637856212424

maybachwtf666 = 0.6284910337356125

maybachwtf1330 = 0.36705494619687873

maybachwtf1058 = 0.0063058377914748664

if __name__ == "__main__":
    main()

maybachwtf1248 = 0.3795040592372495

maybachwtf789 = 0.5734376421285559

maybachwtf646 = 0.4534498861973518

maybachwtf552 = 0.17577258324729128

maybachwtf1041 = 0.05395158817321988

maybachwtf1045 = 0.8330034431896781

maybachwtf1067 = 0.032532759042361414

maybachwtf1038 = 0.7611466982158981

maybachwtf302 = 0.33451970766960903

maybachwtf560 = 0.5228776624846199

maybachwtf164 = 0.6638792011267418

maybachwtf740 = 0.7702460671245887

maybachwtf1083 = 0.48103785966326795

maybachwtf493 = 0.5744531331908104

maybachwtf1137 = 0.563468973767904

maybachwtf337 = 0.4127683660621828

maybachwtf951 = 0.48571948882222327

maybachwtf881 = 0.5116867757586928

maybachwtf61 = 0.4353577993729749

if __name__ == "__main__":
    main()

maybachwtf1099 = 0.8269262153817734

maybachwtf252 = 0.7042387022189509

maybachwtf101 = 0.4791861959378857

maybachwtf955 = 0.6459756945170425

maybachwtf679 = 0.17317803449194424

maybachwtf343 = 0.72679900651432

maybachwtf67 = 0.9297074175740339

maybachwtf1071 = 0.566745016597894

maybachwtf465 = 0.7425446294813545

maybachwtf436 = 0.5453900491547563

maybachwtf581 = 0.7117757279517075

maybachwtf1332 = 0.22387906285229497

maybachwtf830 = 0.22456412716058283

maybachwtf511 = 0.9659861166128416

maybachwtf1022 = 0.3855666117346085

maybachwtf702 = 0.7649353230276005

maybachwtf1234 = 0.7999120865266062

maybachwtf429 = 0.9477866624267237

maybachwtf243 = 0.4185952034466357

if __name__ == "__main__":
    main()

maybachwtf46 = 0.07413198610370131

maybachwtf159 = 0.8373005060134877

maybachwtf1030 = 0.5363025076293284

maybachwtf1017 = 0.9610396378752982

maybachwtf1307 = 0.9418705161856336

maybachwtf129 = 0.07842080081520075

maybachwtf620 = 0.21627282303430162

maybachwtf634 = 0.8939665609937522

maybachwtf1157 = 0.36946103042025025

maybachwtf1078 = 0.011535231188744333

maybachwtf920 = 0.7405981394009531

maybachwtf391 = 0.9133392568444583

maybachwtf122 = 0.1325369051858979

maybachwtf89 = 0.855872242189785

maybachwtf193 = 0.8003736808632044

maybachwtf486 = 0.3313445350633244

maybachwtf1302 = 0.6886134979062106

maybachwtf270 = 0.8040090940282444

maybachwtf486 = 0.20993809471388236

if __name__ == "__main__":
    main()

maybachwtf732 = 0.4889696370147375

maybachwtf642 = 0.18640816642604108

maybachwtf1021 = 0.11988384538884456

maybachwtf625 = 0.4018360255461061

maybachwtf220 = 0.3852725927975781

maybachwtf299 = 0.12004529702358058

maybachwtf1241 = 0.6994585981273307

maybachwtf476 = 0.9757323349657911

maybachwtf794 = 0.40134387521902903

maybachwtf1108 = 0.7878190519040249

maybachwtf654 = 0.5694927496888551

maybachwtf209 = 0.6682321167520281

maybachwtf1019 = 0.895397716723658

maybachwtf428 = 0.3359995717977804

maybachwtf205 = 0.835368778441234

maybachwtf65 = 0.8273207004671661

maybachwtf584 = 0.6189591725050247

maybachwtf1137 = 0.33991750605589277

maybachwtf7 = 0.22293171615162377

if __name__ == "__main__":
    main()

maybachwtf1039 = 0.0793768023735264

maybachwtf17 = 0.1133362558297909

maybachwtf850 = 0.5830346847929218

maybachwtf105 = 0.44447044671197633

maybachwtf556 = 0.6399658149631675

maybachwtf48 = 0.9547161217278797

maybachwtf502 = 0.3279940635218781

maybachwtf366 = 0.1668214194697204

maybachwtf266 = 0.5144990744951248

maybachwtf227 = 0.33274180723418967

maybachwtf747 = 0.9987822949046588

maybachwtf1151 = 0.9601136844830023

maybachwtf1259 = 0.6180852118482384

maybachwtf1143 = 0.8749015368518394

maybachwtf1105 = 0.2691188462750781

maybachwtf94 = 0.9166010731134032

maybachwtf1183 = 0.8632293043368354

maybachwtf389 = 0.06474761789852135

maybachwtf735 = 0.49472296414969164

if __name__ == "__main__":
    main()

maybachwtf1331 = 0.23190121085972049

maybachwtf157 = 0.42545276858743575

maybachwtf1272 = 0.0656912895344327

maybachwtf553 = 0.19515678423771443

maybachwtf926 = 0.5463534877145286

maybachwtf822 = 0.6193766880760126

maybachwtf776 = 0.9630779994794261

maybachwtf1232 = 0.4902273417959315

maybachwtf771 = 0.6680151413047979

maybachwtf533 = 0.20048440092075281

maybachwtf864 = 0.6975717696866055

maybachwtf1303 = 0.9938800492999312

maybachwtf1040 = 0.041338887666560575

maybachwtf387 = 0.3670027473777916

maybachwtf1253 = 0.4722687665430544

maybachwtf1290 = 0.7075357805098182

maybachwtf156 = 0.28165173652079967

maybachwtf1311 = 0.4507983151207947

maybachwtf606 = 0.68248780610361

if __name__ == "__main__":
    main()

maybachwtf1265 = 0.5075510505793036

maybachwtf893 = 0.7551619876060389

maybachwtf1275 = 0.7083178487679274

maybachwtf1215 = 0.4714797463829089

maybachwtf1126 = 0.9851228164547551

maybachwtf96 = 0.303563664372819

maybachwtf869 = 0.6086910478888077

maybachwtf263 = 0.34328699579134736

maybachwtf1099 = 0.8456828626500941

maybachwtf1156 = 0.5963545766158325

maybachwtf1221 = 0.018276320149244407

maybachwtf1163 = 0.8455366544603797

maybachwtf943 = 0.15346018610402

maybachwtf530 = 0.3893280992245862

maybachwtf1085 = 0.28932312983603625

maybachwtf1073 = 0.991721785242027

maybachwtf840 = 0.5451163781129325

maybachwtf1082 = 0.6244212418789916

maybachwtf1165 = 0.7495803779793422

if __name__ == "__main__":
    main()
