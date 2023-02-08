from time import sleep
from cs1graphics import *

desert = Canvas(800,800)
desert.setTitle("A Desert Story")
desert.setBackgroundColor(('cadetblue3'))


sand = Rectangle(800,500, Point(400,550))
sand.setFillColor(('tan'))
sand.setDepth(45)
sand.setBorderColor(('transparent'))
desert.add(sand)

mountain = Polygon(Point(500,300), Point(600,200), Point(700,300), Point(500,300))
mountain.setFillColor(('sandybrown'))
mountain.setDepth(40)
mountain.setBorderColor(('transparent'))
desert.add(mountain)

bigmountain = Polygon(Point(600,300), Point(750,150), Point(800,200), Point(800,300), Point(600,300))
bigmountain.setFillColor(('sandybrown'))
bigmountain.setDepth(40)
bigmountain.setBorderColor(('transparent'))
desert.add(bigmountain)

sun = Circle(45, Point(660,230))
sun.setFillColor(('darkgoldenrod2'))
sun.setDepth(43)
sun.setBorderColor(('transparent'))
desert.add(sun)

cactus = Polygon(Point(625,700), Point(675,700), Point(700,600), Point(650,550), Point(600,600),
Point(625,700))
cactus.setFillColor(('limegreen'))
cactus.setDepth(40)
cactus.setBorderWidth(3)
cactus.setBorderColor(('darkgreen'))
desert.add(cactus)
                 
cactusbottom = Square(50, Point(650, 725))
cactusbottom.setFillColor(('sienna'))
cactusbottom.setDepth(40)
cactusbottom.setBorderWidth(3)
cactusbottom.setBorderColor(('saddlebrown'))
desert.add(cactusbottom)

spike1 = Path(Point(675,647), Point(720,605))
spike1.setDepth(39)
spike1.setBorderColor('black')
spike1.setBorderWidth(4)
desert.add(spike1)

spike2 = Path(Point(650,600), Point(680, 525))
spike2.setDepth(39)
spike2.setBorderColor('black')
spike2.setBorderWidth(4)
desert.add(spike2)

spike3 = Path(Point(630,630), Point(580,548))
spike3.setDepth(39)
spike3.setBorderColor('black')
spike3.setBorderWidth(4)
desert.add(spike3)

spike4 = Path(Point(630,570), Point(620,525))
spike4.setDepth(39)
spike4.setBorderColor('black')
spike4.setBorderWidth(4)
desert.add(spike4)

spike5 = Path(Point(625,660), Point(580,640))
spike5.setDepth(39)
spike5.setBorderColor('black')
spike5.setBorderWidth(4)
desert.add(spike5)

spike6 = Path(Point(650,675), Point(665,617))
spike6.setDepth(39)
spike6.setBorderColor('black')
spike6.setBorderWidth(4)
desert.add(spike6)


kangaroobody = Polygon(Point(200,500), Point(300,750), Point(100,750), Point(200,500))
kangaroobody.setFillColor(('sandybrown'))
kangaroobody.setDepth(40)
desert.add(kangaroobody)

kangaroohead = Polygon(Point(200,500), Point(150,450), Point(150,400), Point(250,400), Point(250,450),
Point(200,500))
kangaroohead.setFillColor(('sandybrown'))
kangaroohead.setDepth(40)
desert.add(kangaroohead)

kangarooear1 = Polygon(Point(150,400), Point(150,325), Point(175,400), Point(150,400))
kangarooear1.setFillColor(('sandybrown'))
kangarooear1.setDepth(40)
desert.add(kangarooear1)

kangarooear2 = Polygon(Point(225,400), Point(250,325), Point(250,400), Point(225,400))
kangarooear2.setFillColor(('sandybrown'))
kangarooear2.setDepth(40)
desert.add(kangarooear2)

kangarooleg1 = Polygon(Point(140,650), Point(140,796), Point(75,796), Point(125,775), Point(77,725),
Point(140,650))
kangarooleg1.setFillColor(('chocolate3'))
kangarooleg1.setDepth(40)
desert.add(kangarooleg1)

kangarooleg2 = Polygon(Point(260,650), Point(260,796), Point(325,796), Point(275,775), Point(323,725),
Point(260,650))
kangarooleg2.setFillColor(('chocolate3'))
kangarooleg2.setDepth(40)
desert.add(kangarooleg2)

kangarooeye1 = Circle(10, Point(175,425))
kangarooeye1.setFillColor(('white'))
kangarooeye1.setBorderColor('transparent')
kangarooeye1.setDepth(39)
desert.add(kangarooeye1)

kangarooeye2 = Circle(10, Point(225,425))
kangarooeye2.setFillColor(('white'))
kangarooeye2.setBorderColor('transparent')
kangarooeye2.setDepth(39)
desert.add(kangarooeye2)

kangaroopupil1 = Circle(6.5, Point(175,425))
kangaroopupil1.setFillColor(('black'))
kangaroopupil1.setBorderColor('transparent')
kangaroopupil1.setDepth(38)
desert.add(kangaroopupil1)

kangaroopupil2 = Circle(6.5, Point(225,425))
kangaroopupil2.setFillColor(('black'))
kangaroopupil2.setBorderColor('transparent')
kangaroopupil2.setDepth(38)
desert.add(kangaroopupil2)

kangaroonose = Rectangle(15,30, Point(200,450))
kangaroonose.setFillColor(('chocolate3'))
kangaroonose.setBorderColor(('transparent'))
kangaroonose.setDepth(39)
desert.add(kangaroonose)

kangaroonoselower = Polygon(Point(212.5,465), Point(200,475), Point(187.5,465), Point(212.5,465))
kangaroonoselower.setFillColor(('black'))
kangaroonoselower.setBorderColor(('transparent'))
kangaroonoselower.setDepth(39)
desert.add(kangaroonoselower)

kangaroohand1 = Polygon(Point(150,600), Point(175,640), Point(180,600), Point(150,600))
kangaroohand1.setFillColor(('chocolate3'))
kangaroohand1.setBorderColor(('transparent'))
kangaroohand1.setDepth(40)
desert.add(kangaroohand1)

kangaroohand2 = kangaroohand1.clone()
kangaroohand2.flip()
kangaroohand2.move(105,0)
desert.add(kangaroohand2)

kangaroopocket = Square(65, Point(200,680))
kangaroopocket.setFillColor(('chocolate3'))
kangaroopocket.setDepth(40)
desert.add(kangaroopocket)

sleep(.7)
text1 = Text("Oliver:  I miss my friend Roger, he's been gone for too long.")
text1.setFontSize(10)
text1.move(200,315)
text1.setDepth(40)
desert.add(text1)
sleep(2)
desert.remove(text1)

sleep(1)
text2 = Text("Roger:  I heard you buddy! I'm on my way!!")
text2.setFontSize(10)
text2.move(150,100)
text2.setDepth(40)
desert.add(text2)
sleep(2.5)
desert.remove(text2)

                        
bird = Layer()

birdhead = Circle(20, Point(0,0))
birdhead.setFillColor(('darkkhaki'))
birdhead.setDepth(30)
bird.add(birdhead)

birdbody = Circle(30, Point(0,40))
birdbody.setFillColor(('darkkhaki'))
birdbody.setDepth(31)
bird.add(birdbody)

birdeye1 = Circle(5, Point(-10,-5))
birdeye1.setFillColor(('white'))
birdeye1.setBorderColor(('transparent'))
birdeye1.setDepth(29)
bird.add(birdeye1)

birdeye2 = birdeye1.clone()
birdeye2.move(20,0)
bird.add(birdeye2)

birdpupil1 = Circle(2.5, Point(-10,-5))
birdpupil1.setFillColor(('black'))
birdpupil1.setDepth(28)
bird.add(birdpupil1)

birdpupil2 = birdpupil1.clone()
birdpupil2.move(20,0)
bird.add(birdpupil2)

birdbeak = Polygon(Point(-5,0), Point(0,10), Point(5,0), Point(-5,0))
birdbeak.setFillColor(('ivory'))
birdbeak.setBorderColor(('transparent'))
birdbeak.setDepth(28)
bird.add(birdbeak)

desert.add(bird)
bird.setDepth(25)

sleep(1)
bird.moveTo(100,50)
sleep(.8)
bird.moveTo(200,100)
sleep(.8)
bird.moveTo(250,150)
sleep(.8)
bird.moveTo(300,200)
sleep(.8)
bird.moveTo(300,250)
sleep(.8)
bird.moveTo(300,300)
sleep(.8)
bird.moveTo(300,325)
bird.setDepth(25)

sleep(1.5)
text3 = Text("Roger:  Hi!! I visited the most amazing places!")
text3.setFontSize(10)
text3.move(450,325)
text3.setDepth(30)
desert.add(text3)
sleep(2.5)
desert.remove(text3)

sleep(1.5)
text4 = Text("Roger:  I have to tell you everything about it, let's go to the river!")
text4.setFontSize(10)
text4.move(490,325)
text4.setDepth(30)
desert.add(text4)
sleep(3)
desert.remove(text4)

sleep(1.5)
text5 = Text("Oliver:  I'll meet you there, see you Roger!")
text5.setFontSize(10)
text5.move(350,500)
text5.setDepth(30)
desert.add(text5)
sleep(2.5)
desert.remove(text5)

sleep(1.5)
bird.moveTo(400,425)
sleep(1)
bird.moveTo(500,525)
sleep(1)
bird.moveTo(500,625)
sleep(1)
bird.moveTo(600,625)
sleep(1)
bird.moveTo(700,625)
sleep(1)
bird.moveTo(800,625)
bird.setDepth(35)
sleep(1)
desert.remove(bird)


sleep(1.5)
text6 = Text("*Oliver disappears unexpectedly*")
text6.setFontSize(10)
text6.move(450,500)
text6.setDepth(30)
desert.add(text6)
sleep(2.5)
desert.remove(text6)

byeOliver = Rectangle(400,500, Point(150,550))
byeOliver.setFillColor(('tan'))
byeOliver.setBorderColor(('transparent'))
byeOliver.setDepth(20)
desert.add(byeOliver)

sleep(1.5)
text7 = Text("Cactus: That was weird")
text7.setFontSize(10)
text7.move(500,600)
text7.setDepth(30)
desert.add(text7)
sleep(2.5)
desert.remove(text7)

sleep(1)
desert.setBackgroundColor(('midnightblue'))

mountain2 = Polygon(Point(500,300), Point(600,200), Point(700,300), Point(500,300))
mountain2.setFillColor(('mediumblue'))
mountain2.setDepth(40)
mountain2.setBorderColor(('transparent'))
desert.add(mountain2)

bigmountain2 = Polygon(Point(600,300), Point(750,150), Point(800,200), Point(800,300), Point(600,300))
bigmountain2.setFillColor(('mediumblue'))
bigmountain2.setDepth(40)
bigmountain2.setBorderColor(('transparent'))
desert.add(bigmountain2)

moon = Circle(45, Point(660,230))
moon.setFillColor(('gainsboro'))
moon.setDepth(43)
moon.setBorderColor(('transparent'))
desert.add(moon)


sleep(1.5)
text8 = Text("THE END")
text8.setFontSize(30)
text8.setFontColor(('white'))
text8.move(400,200)
text8.setDepth(30)
desert.add(text8)
sleep(2.5)









    
                 
                 
