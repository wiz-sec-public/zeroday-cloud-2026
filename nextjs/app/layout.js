export const metadata = {
  title: "zeroday.cloud Next.js target",
  description: "Minimal App Router production target",
};


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
