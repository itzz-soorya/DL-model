<h1 align="center">💪 Fitness Pro - AI Fitness Assistant 🤖</h1>

![Demo App](/public/screenshot-for-readme.png)

## Highlights:

- 🚀 Tech stack: Next.js, React, Tailwind & Shadcn UI
- 🤖 AI Integration (OpenAI, Gemini, with Smart Fallback)
- 🏋️ Personalized Workout Plans
- 🥗 Custom Diet Programs
- � Local Storage
- 🎬 Real-time Program Generation
- 💻 Responsive Design
- 🎭 Client & Server Components

## Features

- **Smart AI Assistant**: Generate personalized fitness plans based on your goals and preferences
- **Personalized Workout Plans**: Get custom exercise routines based on your fitness level, injuries, and goals
- **Diet Recommendations**: Receive personalized meal plans accounting for your allergies and dietary preferences
- **No Authentication Required**: Simple and direct access to fitness planning
- **Smart Fallback System**: Works even without API keys using comprehensive built-in data
- **Responsive Design**: Beautiful UI that works across all devices

## Setup .env file (Optional)

```js
# OpenAI API (Optional - has smart fallback)
OPENAI_API_KEY=your_openai_api_key_here

# Gemini AI (Optional - has smart fallback)
GEMINI_API_KEY=your_gemini_api_key_here
```

Note: API keys are optional. The app includes a comprehensive fallback system with 1000+ exercise and meal combinations that works without any external APIs.

## Getting Started

1. Clone the repository
2. Install dependencies:

```shell
npm install
```

3. Set up your environment variables as shown above
4. Run the development server:

```shell
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## Deployment

This application can be easily deployed to Vercel or any Node.js hosting:

```shell
npm run build
npm run start
```

## Technologies Used

- **Next.js**: React framework for building the frontend and API routes
- **Tailwind CSS & Shadcn UI**: For styling and UI components
- **OpenAI API**: Optional - For AI-generated personalized fitness programs
- **Gemini AI**: Optional - Alternative AI for generating personalized fitness programs
- **Smart Fallback System**: Built-in comprehensive exercise and meal database

## Learn More

To learn more about the technologies used in this project:

- [Next.js Documentation](https://nextjs.org/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Gemini AI Documentation](https://ai.google.dev/gemini-api)
- [Tailwind CSS](https://tailwindcss.com/docs)
