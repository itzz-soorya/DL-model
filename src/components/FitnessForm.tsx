"use client";

import { Button } from "@/components/ui/button";
import { useState } from "react";

interface FitnessFormData {
  fitnessGoals: string;
  fitnessLevel: string;
  injuries: string;
  allergies: string;
  age: string;
  weight: string;
  height: string;
  additionalInfo: string;
}

interface FitnessFormProps {
  onSubmit: (data: FitnessFormData) => void;
  isLoading: boolean;
}

export const FitnessForm = ({ onSubmit, isLoading }: FitnessFormProps) => {
  const [formData, setFormData] = useState<FitnessFormData>({
    fitnessGoals: "",
    fitnessLevel: "",
    injuries: "",
    allergies: "",
    age: "",
    weight: "",
    height: "",
    additionalInfo: "",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="border rounded-lg p-6 bg-white">
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Fitness Goals */}
        <div>
          <label htmlFor="fitnessGoals" className="block text-sm font-medium mb-2 text-gray-900">
            What are your fitness goals? <span className="text-red-500">*</span>
          </label>
          <textarea
            id="fitnessGoals"
            name="fitnessGoals"
            value={formData.fitnessGoals}
            onChange={handleChange}
            required
            rows={3}
            placeholder="e.g., Lose weight, build muscle, improve endurance..."
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>

        {/* Fitness Level */}
        <div>
          <label htmlFor="fitnessLevel" className="block text-sm font-medium mb-2 text-gray-900">
            Current Fitness Level <span className="text-red-500">*</span>
          </label>
          <select
            id="fitnessLevel"
            name="fitnessLevel"
            value={formData.fitnessLevel}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
          >
            <option value="">Select your fitness level</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>

        {/* Physical Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label htmlFor="age" className="block text-sm font-medium mb-2 text-gray-900">
              Age <span className="text-red-500">*</span>
            </label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
              min="1"
              max="120"
              placeholder="25"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
            />
          </div>

          <div>
            <label htmlFor="weight" className="block text-sm font-medium mb-2 text-gray-900">
              Weight (kg) <span className="text-red-500">*</span>
            </label>
            <input
              type="number"
              id="weight"
              name="weight"
              value={formData.weight}
              onChange={handleChange}
              required
              min="1"
              step="0.1"
              placeholder="70"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
            />
          </div>

          <div>
            <label htmlFor="height" className="block text-sm font-medium mb-2 text-gray-900">
              Height (cm) <span className="text-red-500">*</span>
            </label>
            <input
              type="number"
              id="height"
              name="height"
              value={formData.height}
              onChange={handleChange}
              required
              min="1"
              step="0.1"
              placeholder="175"
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
            />
          </div>
        </div>

        {/* Injuries */}
        <div>
          <label htmlFor="injuries" className="block text-sm font-medium mb-2 text-gray-900">
            Any injuries or physical limitations?
          </label>
          <textarea
            id="injuries"
            name="injuries"
            value={formData.injuries}
            onChange={handleChange}
            rows={2}
            placeholder="e.g., Knee pain, lower back issues, or 'None'"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
          />
        </div>

        {/* Allergies */}
        <div>
          <label htmlFor="allergies" className="block text-sm font-medium mb-2 text-gray-900">
            Food allergies or dietary restrictions?
          </label>
          <textarea
            id="allergies"
            name="allergies"
            value={formData.allergies}
            onChange={handleChange}
            rows={2}
            placeholder="e.g., Lactose intolerant, vegetarian, nut allergy, or 'None'"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
          />
        </div>

        {/* Additional Information */}
        <div>
          <label htmlFor="additionalInfo" className="block text-sm font-medium mb-2 text-gray-900">
            Additional information (optional)
          </label>
          <textarea
            id="additionalInfo"
            name="additionalInfo"
            value={formData.additionalInfo}
            onChange={handleChange}
            rows={3}
            placeholder="Any other relevant information about your lifestyle, schedule, preferences..."
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900"
          />
        </div>

        {/* Submit Button */}
        <Button
          type="submit"
          disabled={isLoading}
          className="w-full font-semibold py-3"
        >
          {isLoading ? (
            <span className="flex items-center justify-center">
              <svg
                className="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Generating Your Program...
            </span>
          ) : (
            "Generate My Fitness Program"
          )}
        </Button>
      </form>
    </div>
  );
};
