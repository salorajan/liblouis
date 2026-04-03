# Accessible Braille Studio (brl_louis Edition)

A professional-grade Braille transcription tool built with Streamlit and the custom brl_louis engine.

## Language Table Guide
| Language | Table Name |
| :--- | :--- |
| English (UEB G2) | en-ueb-g2.ctb |
| Spanish | es-g1.ctb |
| Hebrew | he-il.ctb |
| Tamil | ta.ctb |

## Acknowledgments
- Jad Wauthier: Technical Mentor (GitHub.com/BlindTechMage)
- Ms. Jenny: Braille Educator
- Saavi Services for the Blind: Phoenix, AZ

## Developer Usage
If you are a developer using this engine in your own Python projects, import it using the new namespace:

import brl_louis as louis

# Example: Translate a simple sentence
result = louis.translateString(['en-ueb-g2.ctb'], 'Hello World')
print(result[0])
