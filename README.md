# VK User Parser

Этот проект представляет собой скрипт на Python для получения информации о пользователе ВКонтакте, включая его подписчиков, подписки и группы. Информация сохраняется в формате JSON.

## Установка

1. Установите необходимые библиотеки, используя pip:

   ```bash
   pip install requests
   ```
2. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/Rendei/OTRPO_Lab3.git
    cd OTRPO_Lab3
    ```

## Конфигурация

1. Создайте файл config.json в корне проекта и добавьте в него ваш токен доступа к VK API:

    ```json
    {
    "access_token": "YOUR_ACCESS_TOKEN"
    }
    ```
    Замените YOUR_ACCESS_TOKEN на ваш токен доступа.

## Использование

Запустите скрипт из командной строки или терминала:

Для получения информации о текущем пользователе:
   ```bash
   python vk_user_info.py
   ```
Для получения информации о конкретном пользователе:
   ```bash
   python vk_user_info.py --user_id <user_id>
   ```
Для указания пути к файлу результата:
   ```bash
   python vk_user_info.py --result_file <path_to_result_file>
   ```   

## Формат результата
```json

{
    "user_id": 487197074,
    "user_name": "Рендей Крутой",
    "followers_count": 9,
    "subscriptions_count": 3,
    "groups": [
        {
            "id": 58120520,
            "name": "Школа компьютерных наук ТюмГУ",
            "screen_name": "scs_utmn",
            "is_closed": 0,
            "type": "page",
            "is_admin": 0,
            "is_member": 1,
            "is_advertiser": 0,
            "photo_50": "https://sun6-23.userapi.com/s/v1/ig2/urhEk2UujP4RsT0ZjW4gcBcZdv_hV1BLhQsEz69ZRC3yvsCK39Z3KzazsJ09cRng5HeIei_RMZn3CP_H0XUAkSXZ.jpg?quality=95&crop=0,0,1818,1818&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=M8C3XY2tgwBPBTkBjeDj9gM3TFUUt7xuTUqk_cLt3wo&cs=50x50",
            "photo_100": "https://sun6-23.userapi.com/s/v1/ig2/urhEk2UujP4RsT0ZjW4gcBcZdv_hV1BLhQsEz69ZRC3yvsCK39Z3KzazsJ09cRng5HeIei_RMZn3CP_H0XUAkSXZ.jpg?quality=95&crop=0,0,1818,1818&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=M8C3XY2tgwBPBTkBjeDj9gM3TFUUt7xuTUqk_cLt3wo&cs=100x100",
            "photo_200": "https://sun6-23.userapi.com/s/v1/ig2/urhEk2UujP4RsT0ZjW4gcBcZdv_hV1BLhQsEz69ZRC3yvsCK39Z3KzazsJ09cRng5HeIei_RMZn3CP_H0XUAkSXZ.jpg?quality=95&crop=0,0,1818,1818&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=M8C3XY2tgwBPBTkBjeDj9gM3TFUUt7xuTUqk_cLt3wo&cs=200x200"
        },
        {
            "id": 223109094,
            "name": "Мизантроп",
            "screen_name": "club223109094",
            "is_closed": 0,
            "type": "page",
            "is_admin": 0,
            "is_member": 1,
            "is_advertiser": 0,
            "photo_50": "https://sun6-20.userapi.com/s/v1/ig2/HR-J1dG7w9SII759ws1hxLU-ZmWL6TUO-4DaxqJQSliiEBwpAF1wmtJKxVau19RT7clT3Iz20DRfrbXMYR6bJ4bI.jpg?quality=95&crop=250,22,483,483&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480&ava=1&u=hkNCf_PokmPwZTvrKLhJfgz3zOUCL32CbB1EbpQsdPQ&cs=50x50",
            "photo_100": "https://sun6-20.userapi.com/s/v1/ig2/HR-J1dG7w9SII759ws1hxLU-ZmWL6TUO-4DaxqJQSliiEBwpAF1wmtJKxVau19RT7clT3Iz20DRfrbXMYR6bJ4bI.jpg?quality=95&crop=250,22,483,483&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480&ava=1&u=hkNCf_PokmPwZTvrKLhJfgz3zOUCL32CbB1EbpQsdPQ&cs=100x100",
            "photo_200": "https://sun6-20.userapi.com/s/v1/ig2/HR-J1dG7w9SII759ws1hxLU-ZmWL6TUO-4DaxqJQSliiEBwpAF1wmtJKxVau19RT7clT3Iz20DRfrbXMYR6bJ4bI.jpg?quality=95&crop=250,22,483,483&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480&ava=1&u=hkNCf_PokmPwZTvrKLhJfgz3zOUCL32CbB1EbpQsdPQ&cs=200x200"
        },
        {
            "id": 160466638,
            "name": "Программа лояльности ТюмГУ «Вместе»",
            "screen_name": "loyalty_vmeste",
            "is_closed": 0,
            "type": "page",
            "is_admin": 0,
            "is_member": 1,
            "is_advertiser": 0,
            "photo_50": "https://sun6-23.userapi.com/s/v1/ig2/jLi9vN4ga3Fy-z3TmG5u0i3vaj-XOyev7bZc4nQh7uKP8c3gVDdkRpay_npE4W8M33ZGSp7Bo3KOjuOTjkUR8YTa.jpg?quality=95&crop=0,0,2000,2000&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=76cHXgWUcpwEBoqnl5n5TKEHB8V2mfbvTWuZolph-iM&cs=50x50",
            "photo_100": "https://sun6-23.userapi.com/s/v1/ig2/jLi9vN4ga3Fy-z3TmG5u0i3vaj-XOyev7bZc4nQh7uKP8c3gVDdkRpay_npE4W8M33ZGSp7Bo3KOjuOTjkUR8YTa.jpg?quality=95&crop=0,0,2000,2000&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=76cHXgWUcpwEBoqnl5n5TKEHB8V2mfbvTWuZolph-iM&cs=100x100",
            "photo_200": "https://sun6-23.userapi.com/s/v1/ig2/jLi9vN4ga3Fy-z3TmG5u0i3vaj-XOyev7bZc4nQh7uKP8c3gVDdkRpay_npE4W8M33ZGSp7Bo3KOjuOTjkUR8YTa.jpg?quality=95&crop=0,0,2000,2000&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440&ava=1&u=76cHXgWUcpwEBoqnl5n5TKEHB8V2mfbvTWuZolph-iM&cs=200x200"
        }
    ]
}

```
