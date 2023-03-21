# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/dotnet/sdk:7.0 as build-env
WORKDIR /src
COPY ["SentimentAnalysis/SentimentAnalysis/SentimentAnalysis.csproj", "SentimentAnalysis/"]
RUN dotnet restore "SentimentAnalysis/SentimentAnalysis.csproj"
COPY SentimentAnalysis .
RUN dotnet publish -c Release -o /publish

FROM mcr.microsoft.com/dotnet/aspnet:7.0 as runtime
WORKDIR /publish
COPY --from=build-env /publish .
EXPOSE 80
EXPOSE 5001
ENTRYPOINT ["dotnet", "SentimentAnalysis.dll"]
