from sentence_transformers import SentenceTransformer
from scene_function import scenes_responses
import time
import numpy as np

class GameEngine:
    
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.character = None
        self.scenes = {}
        self.responses = {}
        self.similarity_threshold = 0.3
        self.orb_found = False
    
    def set_character(self, c_sheet):
        self.character = c_sheet
    
    def add_scene(self, scene_id, scene_text, context=None, required_race=None, required_profession=None):      
        self.scenes[scene_id] = {
            'text': scene_text,
            'context': context,
            'required_race': required_race,
            'required_profession': required_profession,
            'embedding': self.model.encode(scene_text)
        }     
        if scene_id not in self.responses:
            self.responses[scene_id] = []
    
    def add_response(self, scene_id, input_patterns, response_text, race_mod=None, profession_mod=None, response_image=None):
        
        if isinstance(input_patterns, str):
            input_patterns = [input_patterns]
        
        response = {
            'pattern': input_patterns,
            'text': response_text,
            'race_modifier': race_mod,
            'profession_modifier': profession_mod,
            'image': response_image,
            'embeddings': [self.model.encode(pattern) for pattern in input_patterns]
        }
        self.responses[scene_id].append(response)
        
    def find_best_response(self, user_input, current_scene_id):
      
        if current_scene_id not in self.responses:
            return "No hay respuestas disponibles para esta escena."    
        
        user_embedding = self.model.encode(user_input)
        best_score = -1
        best_response = None
        
        for response in self.responses[current_scene_id]:
            similarities = [np.dot(user_embedding, pattern_embeding)
                            for pattern_embeding in response['embeddings']]
            max_similarity = max(similarities)
            
            if response['race_modifier'] == self.character['Raza'].iloc[0]:
                max_similarity += 0.1
            if response['profession_modifier'] == self.character['Profesión'].iloc[0]:
                max_similarity += 0.1
                
            if max_similarity > best_score:
                best_score = max_similarity
                best_response = response
            
        if best_response:
            if current_scene_id == 1 and "orbe arcano" in best_response["text"].lower():
                self.orb_found = True
        
        if best_score >= 0.7:
            return best_response["text"]
        else:
            return "Tu acción no está contemplada por ahora en el juego. Sé más específico"
            
    
    def load_scenes(self):
        scenes_responses(self)
        
def play_game(c_sheet):
    
    game = GameEngine()
    game.set_character(c_sheet)
    game.load_scenes()
    
    current_scene_id = 1
    
    time.sleep(1.5)
    print("\n" + game.scenes[current_scene_id]['text'])
    
    while True:
        
        user_input = input("> ").lower()
      
        if user_input == "abandonar juego":
            time.sleep(1.5)
            print ("\n" + f'¡Vuelve pronto o nadie podrá detener al dragón!')
            break
          
        response = game.find_best_response(user_input, current_scene_id)
        print("\n" + response)
        
        if current_scene_id == 1 and "dragón" in response.lower():
            current_scene_id = 2
            time.sleep(1.5)
            print("\n" + game.scenes[current_scene_id]["text"])
            continue
                
        if current_scene_id == 2 and "orbe" in response.lower() and game.orb_found:
            current_scene_id = 3
            time.sleep(1.5)
            print("\n" + game.scenes[current_scene_id]["text"])
            break
            
        if current_scene_id == 2 and "con tu muerte" in response.lower():
            current_scene_id = 4
            time.sleep(1.5)
            print("\n" + game.scenes[current_scene_id]["text"])
            break
            
        time.sleep(1)
        print("\n¿Qué más quieres hacer?")