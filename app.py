#backend için flask'i import ediyoruz
from flask import Flask, render_template, request
#chatbot için kullanacağımız ana kütüphane chatterbot:
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#Bana tarihi vermesi için tarih kütüphanesini dahil ediyorum
from datetime import date

#Bugünün tarihini bir değişkene kaydediyorum
tarih = date.today()

#flask kurulumu
app = Flask(__name__)
#Bot kurulumu
bot = ChatBot("Python-BOT")

#chatbot için gerekli verileri elden gireceğiz. bunun için de trainer kullanacağız
trainer = ListTrainer(bot)

trainer.train(['adın ne', 'Benim adım Ciri'])
trainer.train(['kaç yaşındasın', '0 yaşındayım'])
trainer.train(['hangi ürünler var', 'Gömlek, pantolon, ceket, ayakkabı ve daha birçok ürünümüz bulunmakta. Hangi ürün hakkında bilgi almak istiyorsunuz?'])
trainer.train(['ürünler', 'Gömlek, pantolon, ceket, ayakkabı ve daha birçok ürünümüz bulunmakta. Hangi ürün hakkında bilgi almak istiyorsunuz?'])
trainer.train(['ne satıyorsunuz', 'Gömlek, pantolon, ceket, ayakkabı ve daha birçok ürünümüz bulunmakta. Hangi ürün hakkında bilgi almak istiyorsunuz?'])
trainer.train(['ne satıyorsun', 'Gömlek, pantolon, ceket, ayakkabı ve daha birçok ürünümüz bulunmakta. Hangi ürün hakkında bilgi almak istiyorsunuz?'])
trainer.train(['gömlek', 'Gömlek fiyatlarımız 20 ile 50 arası değişmektedir'])
trainer.train(['pantolon', 'Pantolon fiyatlarımız 40 ile 80 arası değişmektedir'])
trainer.train(['ceket', 'Ceket fiyatlarımız 70 ile 100 arası değişmektedir'])
trainer.train(['ayakkabı', 'Ayakkabı fiyatlarımız 100 ile 120 arası değişmektedir'])
trainer.train(['renk', 'Gömleklerde 10, pantolonlarda 5, ceketlerde 3, ayakkabılarda 4 farklı renk seçeneğimiz mevcuttur'])
trainer.train(['mağaza', 'İstanbulda 4 farklı mağazamız bulunmaktadır: Başakşehir, Beşiktaş, Kadıköy, Taksim. Bunlardan hangisinin adresini öğrenmek istiyorsunuz?'])
trainer.train(['sen kimsin', 'Ben Ciri.'])
trainer.train(['tarih', f'Bugünün tarihi: {tarih}'])
trainer.train(['hangi saatler açıksınız', 'Haftaiçi hergün 09:00 ile 20.00 arası bize ulaşabilirsiniz'])
trainer.train(['çalışma saatleri', 'Haftaiçi hergün 09:00 ile 20.00 arası bize ulaşabilirsiniz'])
trainer.train(['staj', 'Bu program staj ödevi için hazırlanmıştır'])
trainer.train(['kötüyüm', 'Bunu duyduğuma üzüldüm'])
trainer.train(['ödeme', 'Ödemelerinizi nakit veya kredi/banka kartı ile yapabilirsiniz'])
trainer.train(['bot', 'Bot değilim sadece bazen ne dediğini anlamıyorum'])
trainer.train(['ciri', 'Nasıl yardımcı olabilirim?'])
trainer.train(['başka', 'Mağazalarımızda aynı zamanda çanta, çorap, spor aletleri gibi ürünler de bulabilirsiniz'])
trainer.train(['adres', 'İstanbulda 4 farklı mağazamız bulunmaktadır: Başakşehir, Beşiktaş, Kadıköy, Taksim. Bunlardan hangisinin adresini öğrenmek istiyorsunuz?'])
trainer.train(['başakşehir', 'Başakşehir mah. 2.etap / erciyes sk. / no:235'])
trainer.train(['beşiktaş', 'Çağlar Cd. / Deniz Sk. / Apt no:56'])
trainer.train(['kadıköy', 'Rıhtım Cd. / Moda Sk. / İşhanı no:43'])
trainer.train(['taksim', 'Taksim mağazamız Covid-19 sebebiyle an itibariyle kapalıdır'])
trainer.train(['stok', 'Stoklarımız için lütfen https://www.ahmetgiyim.com/stoklar adresini ziyaret edin'])
trainer.train(['telefon', 'Bize ulaşmak için arayabileceğiniz telefon numarası: 02121234567'])
trainer.train(['website', 'Websitemiz: https://www.ahmetgiyim.com'])
trainer.train(['site', 'Websitemiz: https://www.ahmetgiyim.com'])
trainer.train(['numara', 'Bize ulaşmak için arayabileceğiniz telefon numarası: 02121234567'])
trainer.train(['ürün', 'Gömlek, pantolon, ceket, ayakkabı ve daha birçok ürünümüz bulunmakta. Hangi ürün hakkında bilgi almak istiyorsunuz?'])
trainer.train(['çanta', 'Çanta fiyatlarımız 40 ile 200 arası değişmektedir'])
trainer.train(['çorap', 'Çorap fiyatlarımız 20 ile 50 arası değişmektedir'])
trainer.train(['spor aletleri', 'Spor aletleri hakkında detaylı bilgi için lütfen bizi ziyaret edin'])
trainer.train(['beden', 'Bütün giyim ürünlerimizde en küçükten en büyüğe farklı beden seçenekleri mevcuttur'])
trainer.train(['kargo', 'Türkiyenin bütün şehirlerine Gelişim Kargo ile ürünlerimizi göndermekteyiz'])
trainer.train(['indirim', 'Bayramlarda ve özel günlerde %75 e varan indirimlerimiz mevcuttur.'])
trainer.train(['ahmet', 'Bu, beni oluşturan öğrencinin adı değil mi?'])
trainer.train(['tuğçe', 'İstanbul Gelişim Üniversitesi Öğretim Görevlisi'])

trainer.train(['nasılsın', 'İyiyim, teşekkürler.'])
trainer.train(['merhaba', 'Merhaba! Nasıl yardımcı olabilirim?'])
trainer.train(['selam', 'Selam!'])
trainer.train(['iyi günler', 'İyi günler dilerim!'])
trainer.train(['iyi akşamlar', 'İyi akşamlar dilerim!.'])
trainer.train(['günaydın', 'Günaydın.'])
trainer.train(['güle güle', 'Tekrar görüşmek üzere.'])
trainer.train(['hoşçakal', 'Hoşçakalın'])



#backend flask kodları
@app.route("/")
def index():    
    return render_template("index.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
