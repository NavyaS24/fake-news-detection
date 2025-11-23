import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";

interface NewsInputProps {
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
}

export const NewsInput = ({ value, onChange, disabled }: NewsInputProps) => {
  return (
    <div className="space-y-3">
      <Label htmlFor="news-text" className="text-lg font-semibold text-foreground">
        Enter News Article
      </Label>
      <Textarea
        id="news-text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
        placeholder="Paste the news article text here..."
        className="min-h-[200px] resize-none text-base bg-card border-2 focus:border-primary transition-colors"
      />
      <p className="text-sm text-muted-foreground">
        {value.length} characters
      </p>
    </div>
  );
};
