# AWS Bedrock Text and Image Generation

This repository demonstrates how to use AWS Bedrock for text and image generation using various models like Amazon Titan, Meta LLaMA, and AI21 Claude.

## Repository Structure

```
.gitignore
amazontitan.py
claude.py
llama3.py
requirements.txt
test.json
generated_images/
    output.png
```

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/hardik7863/AWSBedrock.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure AWS credentials:**

    Run the following command and provide your AWS Access Key ID, Secret Access Key, region, and output format. Ensure that the user has the necessary permissions to use AWS Bedrock.

    ```sh
    aws configure
    ```

## Usage

### Text Generation

#### Using Meta LLaMA

Run the `llama3.py` script to generate text using the Meta LLaMA model:

```sh
python llama3.py
```

#### Using AI21 Claude

Run the `claude.py` script to generate text using the AI21 Claude model:

```sh
python claude.py
```

### Image Generation

#### Using Amazon Titan

Run the `amazontitan.py` script to generate images using the Amazon Titan model:

```sh
python amazontitan.py
```

The generated image will be saved in the `generated_images` directory as `output.png`.

![Generated Image](generated_images/output.png)

## Configuration

You can modify the prompt and other parameters in the respective scripts to customize the text and image generation.

### Example for Amazon Titan

In `amazontitan.py`, you can change the prompt and image generation configuration:

```python
# Example usage
generate_image("A futuristic city skyline at sunset")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.