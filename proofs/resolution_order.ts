// Principle 5. One content model, many audiences.
//
// A portfolio serves role-calibrated variants from one content model.
// Resolution order is alias, then variant, then default fallback.
// Keys are generic audience labels. A request for an unknown audience
// degrades to the default, never to an error.
//
// Run with: npx tsx proofs/resolution_order.ts
//
// Sample output below.
//   (no key)         -> default     : Systems engineer for client operations
//   specialist-role  -> audience-a  : Support operations systems, end to end
//   audience-b       -> audience-b  : Program architecture for small teams
//   unknown-key      -> default     : Systems engineer for client operations

interface Variant {
  audience: string;
  headline: string;
}

const aliases: Record<string, string> = {
  "specialist-role": "audience-a",
  "leadership-role": "audience-b",
};

const variants: Record<string, Variant> = {
  "audience-a": { audience: "audience-a", headline: "Support operations systems, end to end" },
  "audience-b": { audience: "audience-b", headline: "Program architecture for small teams" },
};

const fallback: Variant = { audience: "default", headline: "Systems engineer for client operations" };

function resolve(key?: string): Variant {
  if (key) {
    const resolved = aliases[key] ?? key;
    if (variants[resolved]) return variants[resolved];
  }
  return fallback;
}

const requests: Array<[string, string | undefined]> = [
  ["(no key)", undefined],
  ["specialist-role", "specialist-role"],
  ["audience-b", "audience-b"],
  ["unknown-key", "unknown-key"],
];

for (const [label, key] of requests) {
  const v = resolve(key);
  console.log(`${label.padEnd(16)} -> ${v.audience.padEnd(11)} : ${v.headline}`);
}
