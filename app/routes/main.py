from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.symbol_matcher import SymbolMatcher
from app.extensions import db

bp = Blueprint('main', __name__)
matcher = SymbolMatcher()

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        if symbol:
            matches = matcher.find_matches(symbol)
            return render_template('index.html', 
                                title='Symbol-ID',
                                symbol=symbol,
                                matches=matches)
    return render_template('index.html', title='Symbol-ID')

@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        original = request.form.get('original_symbol')
        vendor = request.form.get('vendor_symbol')
        vendor_name = request.form.get('vendor')
        
        if original and vendor and vendor_name:
            matcher.add_symbol(original, vendor, vendor_name)
            flash('Symbol added successfully!', 'success')
            return redirect(url_for('main.admin'))
            
    return render_template('admin.html', title='Symbol-ID Admin')