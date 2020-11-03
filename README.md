# WhatsApp-Chat-Viz
This project is intended as a data visualization tool for 2-person WhatsApp chat history logs (exported from iOS). The `Chat-History-Prototyping` notebook loads, transforms and visualizes the data in 'chat.txt'. The `Chat-History-Report` notebook then creates a standalone HTML report containing the generated visualizations.

## Instructions
1. Clone or download the repo.
2. In Anaconda Terminal, run `conda env create -f environment.yml` to create the Conda environment used for this project.
3. Ensure your WhatsApp-exported `chat.txt` file is placed in the top level directory.
4. (Optional) Modify the `Chat-History-User-Defined.ipynb` notebook to include any custom slang words / slang variants for the tool to consider as part of its text processing pipeline.
5. Run all cells in the `Chat-History-Prototyping.ipynb` notebook.
6. Run all cells in the `Chat-History-Report.ipynb` notebook.
7. A standalone HTML report titled "Chat-History-Report" will be created in the top level directory. **[Click here](https://htmlpreview.github.io/?https://github.com/shenal-siri/WhatsApp-Chat-Viz/blob/master/Chat-History-Report.html) for a preview of this file.**

## Generating Artificial Chat Data
Running `Script-Generate-Chat-Data-Fake.py` will create a 'chat.txt' file in the same style as a WhatsApp chat log exported form iOS. The same process for generating a report can then be followed as outlined in the **Instructions** section. The parameters for generating this artificial data can be modified in the script.

## Exporting WhatsApp Chat Logs from an iOS Device
1. Open the chat you wish to export.
2. Tap the contact name.
3. Select 'Export Chat'.
4. Select 'Without Media'.
5. The standard iOS options will present themselves for transferring the generated 'chat.txt' file (email, AirDrop, etc.)
6. Ensure the 'chat.txt' file is placed in the top level of your cloned / local repo.

## File Summary
| Filename / Directory                | Description                                                                                    |
| ------------------------------------| ---------------------------------------------------------------------------------------------- |
| `Chat-History-Prototyping.ipynb`    | Main notebook - loads, transforms and visualizes the data in 'chat.txt'| 
| `Chat-History-Report.ipynb`         | Secondary notebook - creates a standalone HTML report containing the generated visualizations |
| `Chat-History-Report.html`          | Output - report containing chat statistics and visualizations, formatted as HTML |
| `Chat-History-User-Defined.ipynb`   | Supplementary notebook - stores dictionaries for user-defined slang and slang variants |
| `Script-Generate-Chat-Report.ipynb` | Supplementary notebook - called by `Chat-History-Report.ipynb` to generate HTML report |
| `Script-Generate-Chat-Data-Fake.py` | Supplementary script - used to generate artificial 'chat.txt' file for demoing chat vis tool |
| `Script-SVG-to-PNG.py`              | Supplementary script - used to covert emoji images from SVG to PNG with specified dimensions |
| `resources`                         | Contains saved visualization images from chat report, emoji images, and input text for chat generator |

## Potential Future Work
This project is a beginner's foray into data loading, transformation and visualization within 'traditional' data science frameworks offered by Python. As such, there is a significant amount of additional exploration that can be done. For instance:
1. **Implementing machine learning methods** to truly leverage the cleaned and processed chat dataset. [Unsupervised Sentiment Analysis](https://medium.com/@Intellica.AI/vader-ibm-watson-or-textblob-which-is-better-for-unsupervised-sentiment-analysis-db4143a39445) could be a potentially interesting undertaking.
2. **Interactive data visualizations.** Leveraging data visualization frameworks which are not Python-based (such as Power BI or Tableau) would certainly elevate the visualization tool (above the current, simple 'HTML report' implementation).
3. **Creating a web app.** While chat history visualization web apps are certainly [not a novel concept](https://www.google.com/search?q=chat+history+visualizer&oq=chat+history+visualizer&aqs=chrome..69i57.5594j0j7&sourceid=chrome&ie=UTF-8), implementing one would be a good exploration into web development technologies / frameworks.
