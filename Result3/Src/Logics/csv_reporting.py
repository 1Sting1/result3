from Src.Logics.reporting import reporting


class csv_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = ""
        items = self.data[ typeKey ]
        for field in self.fields:
            result += f"{field};"
        return result
        
        
        