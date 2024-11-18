from app import create_app
from app.extensions import db
from datetime import datetime

class Symbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_symbol = db.Column(db.String(50), index=True, nullable=False)
    vendor_symbol = db.Column(db.String(50), index=True, nullable=False)
    vendor = db.Column(db.String(50), index=True)  # Ejemplo: Bloomberg, Reuters, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_used = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Symbol {self.original_symbol} -> {self.vendor_symbol}>'

class SymbolMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String(50), nullable=False)
    matched_symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'), nullable=False)
    confidence = db.Column(db.Float)  # Para cuando implementemos AI
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    matched_symbol = db.relationship('Symbol', backref=db.backref('matches', lazy=True))