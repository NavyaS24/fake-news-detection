import { useState } from "react";
import { Shield, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/button";
import { NewsInput } from "@/components/NewsInput";
import { AnalysisResult } from "@/components/AnalysisResult";
import { toast } from "sonner";

const Index = () => {
  const [newsText, setNewsText] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<{
    isFake: boolean;
    confidence: number;
    analysis: string;
  } | null>(null);

  const analyzeNews = async () => {
    if (!newsText.trim()) {
      toast.error("Please enter some text to analyze");
      return;
    }

    setIsAnalyzing(true);
    setResult(null);

    // Simulate API call with mock analysis
    await new Promise(resolve => setTimeout(resolve, 2000));

    // Mock detection logic based on keywords
    const lowerText = newsText.toLowerCase();
    const fakeIndicators = ["click here", "you won't believe", "shocking", "miracle cure", "one weird trick"];
    const hasFakeIndicators = fakeIndicators.some(indicator => lowerText.includes(indicator));
    
    const isFake = hasFakeIndicators || Math.random() > 0.6;
    const confidence = Math.floor(Math.random() * 20) + 75;

    setResult({
      isFake,
      confidence,
      analysis: isFake
        ? "Our analysis detected patterns commonly associated with misleading content, including sensational language, lack of credible sources, and manipulative phrasing."
        : "The text appears to follow journalistic standards with factual language and credible presentation. However, always verify with multiple sources."
    });

    setIsAnalyzing(false);
    toast.success("Analysis complete!");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-secondary/30 to-background">
      {/* Header */}
      <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-10">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-br from-primary to-primary/70 rounded-lg shadow-lg">
              <Shield className="h-6 w-6 text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-foreground">Fake News Detector</h1>
              <p className="text-sm text-muted-foreground">AI-Powered News Verification</p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="space-y-6">
          {/* Info Card */}
          <div className="bg-card border rounded-xl p-6 shadow-sm">
            <div className="flex items-start gap-3">
              <Sparkles className="h-5 w-5 text-primary mt-1 flex-shrink-0" />
              <div>
                <h2 className="font-semibold text-foreground mb-2">How it works</h2>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  This tool uses machine learning to analyze news articles and detect potential misinformation. 
                  Paste any news text below and our AI will evaluate its credibility based on linguistic patterns, 
                  writing style, and content structure.
                </p>
              </div>
            </div>
          </div>

          {/* Analysis Section */}
          <div className="bg-card border rounded-xl p-6 shadow-sm space-y-6">
            <NewsInput 
              value={newsText}
              onChange={setNewsText}
              disabled={isAnalyzing}
            />

            <Button
              onClick={analyzeNews}
              disabled={isAnalyzing || !newsText.trim()}
              className="w-full h-12 text-base font-semibold shadow-lg hover:shadow-xl transition-all"
              size="lg"
            >
              {isAnalyzing ? (
                <>
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-primary-foreground mr-2" />
                  Analyzing...
                </>
              ) : (
                <>
                  <Shield className="mr-2 h-5 w-5" />
                  Analyze News
                </>
              )}
            </Button>
          </div>

          {/* Results */}
          {result && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
              <AnalysisResult result={result} />
            </div>
          )}

          {/* Disclaimer */}
          <div className="bg-muted/50 border border-border/50 rounded-lg p-4">
            <p className="text-xs text-muted-foreground text-center">
              <strong>Disclaimer:</strong> This is a demonstration interface. For production use, connect to your trained ML model via API. 
              Always verify news from multiple credible sources.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Index;
