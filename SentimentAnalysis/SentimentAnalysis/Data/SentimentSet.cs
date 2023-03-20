using System.Text.Json;
using System.Text.Json.Serialization;

namespace SentimentAnalysis.Data
{
    public class SentimentSet
    {
        [JsonPropertyName("text")]
        public string? Text { get; set; }

        [JsonPropertyName("sentiment")]
        public string? Sentiment { get; set; }

        [JsonPropertyName("value")]
        public double Value { get; set; }
    }
}