from confluent_kafka.admin import AdminClient, NewTopic


def create_topics():
    admin_client = AdminClient({'bootstrap.servers': 'kafka1:29092'})

    topic_list = [
        NewTopic("amur_topic", 1, 1),
        NewTopic("neva_topic", 1, 1),
        NewTopic("ob_topic", 1, 1),
        NewTopic("volga_topic", 1, 1),
        NewTopic("yenisei_topic", 1, 1)
    ]
    admin_client.create_topics(topic_list)

    print(admin_client.list_topics().topics)
