from research.search import search_web
TOPICS=["Python engineering practices","secure coding and defensive security","GitHub developer automation","Termux Android Python tooling"]
class LearningWorker:
    def __init__(self,brain,memory):self.brain=brain;self.memory=memory
    def run_once(self):
        n=0
        for topic in TOPICS:
            hits=search_web(topic)
            if not hits:continue
            text="\n".join(f"{h['title']}\n{h['url']}\n{h['snippet']}" for h in hits)
            note=self.brain.ask("Create concise technical notes with source URLs, caveats, and practice ideas. Don't claim verification.\n"+text)
            self.memory.save("learning",topic,note); n+=1
        return f"Cycle complete: {n} topic summaries stored (when Sheets is configured)."
