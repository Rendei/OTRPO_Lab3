import argparse
import json
import logging
from neo4j_handler import Neo4jHandler
from vk_user_parser import get_vk_user_info

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для загрузки токена и других параметров из конфигурации
def load_config(config_file='OTRPO_Lab4/config.json'):
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скрипт для получения данных ВК и работы с Neo4j')
    parser.add_argument('--user_id', type=str, help='Идентификатор пользователя ВК')
    parser.add_argument('--query', type=str, help='Тип запроса к Neo4j: users_count, groups_count, top_users_by_followers, top_groups_by_subscribers, mutual_followers')

    args = parser.parse_args()

    # Загружаем конфигурацию
    config = load_config()

    # Подключаемся к Neo4j
    neo4j_handler = Neo4jHandler(config['neo4j_uri'], config['neo4j_user'], config['neo4j_password'])

    if args.query:
        # Выполняем запрос к Neo4j
        result = neo4j_handler.query_neo4j(args.query)
        for record in result:
            print(record)
    else:
        # Получаем данные о пользователе и сохраняем в Neo4j
        get_vk_user_info(config, neo4j_handler, args.user_id)

    neo4j_handler.close()
