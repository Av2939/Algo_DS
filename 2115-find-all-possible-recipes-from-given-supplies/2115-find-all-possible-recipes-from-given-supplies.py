class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        ingredient_to_recipe = collections.defaultdict(set)
        ans = []
        in_degree = Counter()
        
        for ingredient, rcp in zip(ingredients, recipes):
            
            not_available = 0
            
            for ing in ingredient:
                
                if ing not in available:
                    not_available += 1
                    ingredient_to_recipe[ing].add(rcp)
            
            if not_available == 0:
                ans.append(rcp)
            else:
                in_degree[rcp] = not_available
                
        
        for rcp in ans:
            for recipe in ingredient_to_recipe.pop(rcp, set()):
                in_degree[recipe] -= 1
                
                if in_degree[recipe] == 0:
                    ans.append(recipe)
                    
        return ans