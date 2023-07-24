# AutoGPT-RabbitMQ

This plugin allows Auto-GPT to search news in Google news.

You can try it right now for free https://ai-autopilot.io

## 📚 Requirements

1. Python Package: Install the pika Python package: 

xml
json
re
urllib.parse
base64
requests


## ⚙️ Installation

Follow these steps to configure the Auto-GPT RabbitMQ Plugin:

1. Clone this Repository

    ```git
    git clone https://github.com/tomtom94/AutoGPT-GoogleNews.git
    ```

2. Navigate to the folder

    ```sh
    cd AutoGPT-GoogleNews
    ```

3. Move the folder google_news_search

    Move the folder `google_news_search` to the `Auto-GPT` plugins directory, there should already be a file there titled `__PUT_PLUGIN_ZIPS_HERE__`.

## 🔧 Configuration

1. Add new entry in the plugins_config.yaml file in `Auto-GPT`:

google_news_search:
  enabled: true
  config: {}
