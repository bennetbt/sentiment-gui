using SentimentAnalysis.Data;

namespace SentimentAnalysis.Services
{
    public class AppData
    {
        public bool LoggedIn { get; set; }
        public List<SentimentSet> Sentiments { get; set; } = new List<SentimentSet>();
    }
}
