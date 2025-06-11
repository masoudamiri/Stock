from django.shortcuts import render
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from django.conf import settings
import os

def chart_view(request):
    file_path = os.path.join(settings.BASE_DIR,'data', 'ABAD.csv')
    df = pd.read_csv(file_path)
    df['<DTYYYYMMDD>'] = pd.to_datetime(df['<DTYYYYMMDD>'], format='%Y%m%d')

    # اطمینان از عددی بودن TradedShare
    df['TradedShare'] = pd.to_numeric(df['TradedShare'], errors='coerce').fillna(0)

    # محدوده محور y کندل‌ها برای تنظیم نسبت ارتفاع میله‌ها
    max_price = df['<HIGH>'].max()
    min_price = df['<LOW>'].min()
    price_range = max_price - min_price

    # نرمال‌سازی حجم درصدی و تبدیل آن به مقدار قابل مقایسه با قیمت‌ها
    df['VolumeHeight'] = (df['TradedShare'] / 100.0) * price_range

    # کندل‌استیک
    candle = go.Candlestick(
        x=df['<DTYYYYMMDD>'],
        open=df['<OPEN>'],
        high=df['<HIGH>'],
        low=df['<LOW>'],
        close=df['<CLOSE>'],
        yaxis='y1',
        name='Price'
    )

    # Bar chart برای TradedShare
    volume = go.Bar(
        x=df['<DTYYYYMMDD>'],
        y=df['VolumeHeight'],
        yaxis='y1',  # مشترک با y1 تا کنار قیمت بیاد
        name='Traded Share (%)',
        marker_color='rgba(255,0,0,1)',
    )

    layout = go.Layout(
        title='ABAD Candlestick + TradedShare (%)',
        xaxis=dict(
            rangeslider=dict(visible=True),
            showticklabels=True
        ),
        yaxis=dict(
            title='Price',
            side='right'
        ),
        height=800,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )

    fig = go.Figure(data=[volume, candle], layout=layout)

    chart_html = pio.to_html(fig, full_html=False)
    return render(request, 'charts/index.html', {'chart': chart_html})


