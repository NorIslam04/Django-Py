from django.shortcuts import render
from django.http import HttpResponse as hr


def index(req):
    return hr("""
            <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Accueil</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 20px;
                color: #f0a500;
            }
            p {
                font-size: 1.2rem;
                color: #cccccc;
            }
            .container {
                padding: 20px;
                border-radius: 10px;
                background-color: #1e1e1e;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenue sur la page d'accueil</h1>
            <p>Explorez un monde de beauté sombre et élégante.</p>
        </div>
    </body>
    </html>
              """)

