export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response("NA Bot is running!");
    }

    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405 });
    }

    const update = await request.json();

    if (update.message?.text === "/start") {
      const chatId = update.message.chat.id;

      const text = `أهلاً بك في زمالة المدمنين المجهولين ❤️

هنا تقدر تلاقي معلومات وروابط تساعدك في طريق التعافي.

اختر من القائمة:`;

      const keyboard = {
        inline_keyboard: [
          [
            {
              text: "💬 جروب واتساب للأعضاء",
              url: "https://chat.whatsapp.com/GjK95H7HePf3ERdT95QFgj"
            }
          ],
          [
            {
              text: "📍 أماكن اجتماعات إقليم مصر",
              url: "https://naegypt.org/ar/meetings"
            }
          ],
          [
            {
              text: "🌍 موقع الزمالة العالمي",
              url: "https://m.na.org/"
            }
          ]
        ]
      };

      await fetch(`https://api.telegram.org/bot${env.BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          chat_id: chatId,
          text: text,
          reply_markup: keyboard
        })
      });
    }

    return new Response("OK");
  }
};
