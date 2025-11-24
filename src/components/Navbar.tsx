"use client";

import { DumbbellIcon, ZapIcon } from "lucide-react";
import Link from "next/link";
import { Button } from "./ui/button";

const Navbar = () => {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-background/60 backdrop-blur-md border-b border-border py-3">
      <div className="container mx-auto flex items-center justify-between">
        {/* LOGO */}
        <Link href="/" className="flex items-center gap-2">
          <div className="p-1 bg-primary/10 rounded">
            <ZapIcon className="w-4 h-4 text-primary" />
          </div>
          <span className="text-xl font-bold font-mono">
            Fitness<span className="text-primary">Pro</span>
          </span>
        </Link>

        {/* NAVIGATION */}
        <nav className="flex items-center gap-5">
          <Button
            asChild
            className="bg-primary text-primary-foreground hover:bg-primary/90"
          >
            <Link href="/generate-program">
              <DumbbellIcon className="w-4 h-4 mr-2" />
              Generate Plan
            </Link>
          </Button>
        </nav>
      </div>
    </header>
  );
};
export default Navbar;
