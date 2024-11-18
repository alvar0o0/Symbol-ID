from app.models.symbol import Symbol
from app.extensions import db
from sqlalchemy import or_

class SymbolMatcher:
    def find_matches(self, symbol):
        """
        Encuentra símbolos similares usando métodos más sofisticados
        """
        matches = {
            'exact': self._exact_match(symbol),
            'fuzzy': self._fuzzy_match(symbol),
            'pattern': self._pattern_match(symbol),
            'normalized': self._normalized_match(symbol)
        }
        # Agregar score/confidence a cada match
        return self._rank_matches(matches)
    
    def _normalized_match(self, symbol):
        """
        Normaliza símbolos removiendo espacios, caracteres especiales
        Ej: "BRK-B" matchearía con "BRK.B", "BRK B", "BRKB"
        """
        normalized_symbol = self._normalize_symbol(symbol)
        matches = Symbol.query.filter(
            self._normalize_symbol(Symbol.original_symbol) == normalized_symbol
        ).all()
        return [match.vendor_symbol for match in matches]
    
    def _pattern_match(self, symbol):
        """
        Busca patrones comunes en símbolos financieros
        Ej: "AAPL US" matchearía con "AAPL.N", "AAPL.O", "AAPL US Equity"
        """
        base_symbol = self._extract_base_symbol(symbol)
        matches = Symbol.query.filter(
            Symbol.original_symbol.startswith(base_symbol)
        ).all()
        return [match.vendor_symbol for match in matches]
    
    def _fuzzy_match(self, symbol):
        """
        Usa algoritmos de fuzzy matching para encontrar símbolos similares
        """
        from fuzzywuzzy import fuzz
        
        all_symbols = Symbol.query.all()
        fuzzy_matches = []
        
        for db_symbol in all_symbols:
            ratio = fuzz.ratio(symbol.lower(), db_symbol.original_symbol.lower())
            if ratio > 80:  # umbral configurable
                fuzzy_matches.append(db_symbol.vendor_symbol)
        
        return fuzzy_matches
    
    @staticmethod
    def _normalize_symbol(symbol):
        """
        Normaliza un símbolo financiero
        """
        import re
        # Remover espacios y caracteres especiales
        normalized = re.sub(r'[^a-zA-Z0-9]', '', symbol.upper())
        return normalized
    
    @staticmethod
    def _extract_base_symbol(symbol):
        """
        Extrae el símbolo base sin sufijos de mercado
        """
        # Implementar lógica para extraer símbolo base
        # Ej: "AAPL US" -> "AAPL"
        pass
    
    def _rank_matches(self, matches):
        """
        Asigna un score a cada match y ordena los resultados
        """
        # Implementar lógica de ranking
        pass