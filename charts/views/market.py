from django.shortcuts import render
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from django.conf import settings
import os

def market_view(request):
    base = 1000000.0
    file_path = os.path.join(settings.BASE_DIR, 'data', 'ABAD-P1.csv')
    
    # خواندن دیتا
    df = pd.read_csv(file_path)
    df['<DTYYYYMMDD>'] = pd.to_datetime(df['<DTYYYYMMDD>'], format='%Y%m%d')

    # تبدیل حجم بازار به عدد و جلوگیری از NaN
    df['TradedOfTotalMarket'] = pd.to_numeric(df['TradedOfTotalMarket'], errors='coerce').fillna(0)

    # محاسبه محدوده قیمت برای نرمال‌سازی ارتفاع بارها
    max_price = df['<HIGHMarketValue>'].max()
    min_price = df['<LOWMarketValue>'].min()
    price_range = (max_price - min_price) / base
    df['VolumeHeight'] = (df['TradedOfTotalMarket'] / 100.0) * price_range

    # کندل‌استیک
    candle = go.Candlestick(
        x=df['<DTYYYYMMDD>'],
        open=df['<OPENMarketValue>'] / base,
        high=df['<HIGHMarketValue>'] / base,
        low=df['<LOWMarketValue>'] / base,
        close=df['<CloseMarketValue>'] / base,
        yaxis='y1',
        name='Value'
    )

    # نمودار میله‌ای حجم
    volume = go.Bar(
        x=df['<DTYYYYMMDD>'],
        y=df['VolumeHeight'],
        yaxis='y1',
        name='Total Market (%)',
        marker_color='rgba(255,0,0,1)',
    )

    # نمایش فقط آخرین 100 روز به صورت پیش‌فرض
    if len(df) >= 100:
        start_date = df['<DTYYYYMMDD>'].iloc[-100]
    else:
        start_date = df['<DTYYYYMMDD>'].iloc[0]
    end_date = df['<DTYYYYMMDD>'].iloc[-1]

    # تنظیمات چارت
    layout = go.Layout(
        title='ABAD Candlestick + TradedShare (%)',
        xaxis=dict(
            rangeslider=dict(visible=True),
            range=[start_date, end_date],
            showticklabels=True
        ),
        yaxis=dict(
            title='Price',
            side='right'
        ),
        height=800,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True
    )

    # ساخت شکل نهایی
    fig = go.Figure(data=[volume, candle], layout=layout)

    # تبدیل به HTML برای درج در قالب
    chart_html = pio.to_html(fig, full_html=False, config={
        'scrollZoom': True,
        'displayModeBar': False
    })

    return render(request, 'charts/market.html', {'chart': chart_html})
