import { Button } from "@/components/ui/button";
import { DumbbellIcon } from "lucide-react";
import Link from "next/link";

const HomePage = () => {
  return (
    <div className="flex items-center justify-center min-h-screen p-4 bg-white">
      <div className="max-w-2xl w-full text-center space-y-6">
        <h1 className="text-4xl md:text-5xl font-bold text-gray-900">
          Fitness Plan Generator
        </h1>
        
        <p className="text-lg text-gray-700">
          Create your personalized workout and diet plan
        </p>

        <Button
          size="lg"
          asChild
          className="px-8 py-6 text-lg"
        >
          <Link href="/generate-program">
            <DumbbellIcon className="mr-2 h-5 w-5" />
            Get Started
          </Link>
        </Button>
      </div>
    </div>
  );
};

export default HomePage;
