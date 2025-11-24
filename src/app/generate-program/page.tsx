"use client";

import { FitnessForm } from "@/components/FitnessForm";
import { useRouter } from "next/navigation";
import { useState } from "react";

const GenerateProgramPage = () => {
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const router = useRouter();

  const handleFormSubmit = async (formData: any) => {
    try {
      setIsGenerating(true);
      setError(null);

      // Call API route to generate fitness plan
      const response = await fetch("/api/generate-plan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Failed to generate fitness plan");
      }

      const data = await response.json();
      
      // Save to localStorage
      localStorage.setItem("fitnessPlan", JSON.stringify(data));

      setSuccess(true);
      
      setTimeout(() => {
        router.push("/profile");
      }, 2000);
    } catch (err) {
      console.error("Error generating fitness plan:", err);
      setError(
        err instanceof Error ? err.message : "Failed to generate fitness program. Please try again."
      );
      setIsGenerating(false);
    }
  };

  return (
    <div className="flex flex-col min-h-screen p-4 md:p-8 bg-gray-50">
      <div className="container mx-auto max-w-3xl">
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold mb-2 text-gray-900">
            Generate Your Fitness Plan
          </h1>
          <p className="text-gray-700">
            Fill out the form below to create your personalized plan
          </p>
        </div>

        {success && (
          <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
            <div className="flex items-center gap-3">
              <div className="w-6 h-6 rounded-full bg-green-500 flex items-center justify-center text-white">
                ✓
              </div>
              <div>
                <h3 className="font-semibold text-green-700">Success!</h3>
                <p className="text-sm text-green-600">
                  Your fitness program has been created! Redirecting to your profile...
                </p>
              </div>
            </div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <div className="flex items-center gap-3">
              <div className="w-6 h-6 rounded-full bg-red-500 flex items-center justify-center text-white">
                ✕
              </div>
              <div>
                <h3 className="font-semibold text-red-700">Error</h3>
                <p className="text-sm text-red-600">{error}</p>
              </div>
            </div>
          </div>
        )}

        <FitnessForm onSubmit={handleFormSubmit} isLoading={isGenerating} />
      </div>
    </div>
  );
};

export default GenerateProgramPage;
