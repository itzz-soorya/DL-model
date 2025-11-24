"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { AppleIcon, CalendarIcon, DumbbellIcon, DownloadIcon } from "lucide-react";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import Link from "next/link";

const ProfilePage = () => {
  const [plan, setPlan] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Load plan from localStorage
    const savedPlan = localStorage.getItem("fitnessPlan");
    if (savedPlan) {
      setPlan(JSON.parse(savedPlan));
    }
    setLoading(false);
  }, []);

  const downloadPlan = () => {
    if (!plan) return;

    const dataStr = JSON.stringify(plan, null, 2);
    const dataBlob = new Blob([dataStr], { type: "application/json" });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `fitness-plan-${new Date().toISOString().split("T")[0]}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <p className="text-gray-700">Loading...</p>
      </div>
    );
  }

  if (!plan) {
    return (
      <div className="flex items-center justify-center min-h-screen p-4 bg-gray-50">
        <div className="text-center space-y-4 max-w-md">
          <DumbbellIcon className="w-16 h-16 text-gray-400 mx-auto" />
          <h2 className="text-2xl font-semibold text-gray-900">No Plan Yet</h2>
          <p className="text-gray-700">
            Generate your personalized fitness and diet plan.
          </p>
          <Button asChild>
            <Link href="/generate-program">Generate Plan</Link>
          </Button>
        </div>
      </div>
    );
  }

  const { workoutPlan, dietPlan, generatedAt } = plan;

  return (
    <div className="min-h-screen p-4 md:p-8 bg-gray-50">
      <div className="container mx-auto max-w-4xl">
        {/* Header */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between mb-6 gap-4">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Your Fitness Plan</h1>
            <p className="text-gray-700 text-sm mt-1">
              Generated on {new Date(generatedAt).toLocaleDateString()}
            </p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" onClick={downloadPlan} size="sm" className="bg-white text-gray-900 border-gray-300 hover:bg-gray-50">
              <DownloadIcon className="w-4 h-4 mr-2" />
              Download
            </Button>
            <Button asChild size="sm" className="bg-blue-600 text-white hover:bg-blue-700">
              <Link href="/generate-program">Regenerate</Link>
            </Button>
          </div>
        </div>

      {/* Tabs for Workout and Diet */}
      <Tabs defaultValue="workout" className="w-full">
        <TabsList className="grid w-full grid-cols-2 max-w-md mx-auto mb-8">
          <TabsTrigger value="workout" className="flex items-center gap-2">
            <DumbbellIcon size={16} />
            Workout Plan
          </TabsTrigger>
          <TabsTrigger value="diet" className="flex items-center gap-2">
            <AppleIcon size={16} />
            Diet Plan
          </TabsTrigger>
        </TabsList>

        {/* Workout Plan Tab */}
        <TabsContent value="workout" className="space-y-6">
          <div className="border rounded-lg p-6 bg-white">
            <div className="flex items-center gap-3 mb-6">
              <CalendarIcon className="w-6 h-6 text-gray-900" />
              <div>
                <h2 className="text-xl font-bold text-gray-900">Weekly Schedule</h2>
                <p className="text-gray-700 text-sm">
                  {workoutPlan.schedule.join(" • ")}
                </p>
              </div>
            </div>

            <Accordion type="single" collapsible className="w-full">
              {workoutPlan.exercises.map((exercise: any, idx: number) => (
                <AccordionItem key={idx} value={`day-${idx}`}>
                  <AccordionTrigger className="text-lg font-semibold text-gray-900">
                    <div className="flex items-center gap-3">
                      <span>{exercise.day}</span>
                      <span className="text-sm text-gray-500 font-normal">
                        ({exercise.routines.length} exercises)
                      </span>
                    </div>
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="space-y-3 pt-4">
                      {exercise.routines.map((routine: any, rIdx: number) => (
                        <div
                          key={rIdx}
                          className="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
                        >
                          <div>
                            <h4 className="font-semibold text-gray-900">{routine.name}</h4>
                          </div>
                          <div className="flex gap-4 text-sm text-gray-600">
                            <span>
                              <strong className="text-gray-900">{routine.sets}</strong> sets
                            </span>
                            <span>
                              <strong className="text-gray-900">{routine.reps}</strong> reps
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </div>
        </TabsContent>

        {/* Diet Plan Tab */}
        <TabsContent value="diet" className="space-y-6">
          <div className="border rounded-lg p-6 bg-white">
            <div className="mb-6">
              <h2 className="text-xl font-bold text-gray-900">Daily Nutrition</h2>
              <p className="text-gray-700 text-sm mt-1">
                Target: <strong className="text-gray-900">{dietPlan.dailyCalories}</strong> calories/day
              </p>
            </div>

            <div className="space-y-4">
              {dietPlan.meals.map((meal: any, idx: number) => (
                <div key={idx} className="p-4 bg-gray-50 rounded-lg">
                  <h3 className="font-semibold text-lg mb-3 text-gray-900">
                    {meal.name}
                  </h3>
                  <ul className="space-y-2 ml-4">
                    {meal.foods.map((food: string, fIdx: number) => (
                      <li key={fIdx} className="flex items-start gap-2">
                        <span className="mt-1 text-gray-900">•</span>
                        <span className="text-gray-700">{food}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        </TabsContent>
      </Tabs>
      </div>
    </div>
  );
};

export default ProfilePage;
