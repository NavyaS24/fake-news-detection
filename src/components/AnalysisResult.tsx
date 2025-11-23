import { CheckCircle2, AlertTriangle, TrendingUp } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";

interface AnalysisResultProps {
  result: {
    isFake: boolean;
    confidence: number;
    analysis: string;
  } | null;
}

export const AnalysisResult = ({ result }: AnalysisResultProps) => {
  if (!result) return null;

  const { isFake, confidence, analysis } = result;

  return (
    <Card className={`border-2 ${isFake ? 'border-warning bg-warning/5' : 'border-success bg-success/5'}`}>
      <CardHeader>
        <CardTitle className="flex items-center gap-3">
          {isFake ? (
            <>
              <AlertTriangle className="h-6 w-6 text-warning" />
              <span className="text-warning">Fake News Detected</span>
            </>
          ) : (
            <>
              <CheckCircle2 className="h-6 w-6 text-success" />
              <span className="text-success">Appears to be Real News</span>
            </>
          )}
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium flex items-center gap-2">
              <TrendingUp className="h-4 w-4" />
              Confidence Score
            </span>
            <span className="text-lg font-bold">{confidence}%</span>
          </div>
          <Progress 
            value={confidence} 
            className={`h-2 ${isFake ? '[&>div]:bg-warning' : '[&>div]:bg-success'}`}
          />
        </div>
        
        <div className="pt-2 border-t">
          <p className="text-sm text-muted-foreground leading-relaxed">
            {analysis}
          </p>
        </div>
      </CardContent>
    </Card>
  );
};
