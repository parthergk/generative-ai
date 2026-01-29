class Change:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water, milk  , tea, leamon"

# clean = Change.clean_ingredients(raw)
print(Change.clean_ingredients(raw))

obj = Change()

print(obj.clean_ingredients(raw))