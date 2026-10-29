import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ModelMind | More Practice",
  description:
    "Practice Machine Learning through coding, debugging, mathematics and model-based questions.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}