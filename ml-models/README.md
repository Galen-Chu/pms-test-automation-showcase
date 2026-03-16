# ML Models Directory

This directory should contain the trained machine learning models for CAPTCHA solving.

## Required Files

- `captcha_model.keras` - Trained Keras model for CAPTCHA recognition
- `char_mappings.pkl` - Pickled character mappings for decoding predictions

## Note

These model files are not included in the repository due to their large size. 
They are ignored by `.gitignore`.

## Setup

1. Train your CAPTCHA model or obtain pre-trained models
2. Place the model files in this directory:
   - `captcha_model.keras`
   - `char_mappings.pkl`
3. Ensure the files are properly loaded by the application

For more information, see the CAPTCHA solving documentation.
