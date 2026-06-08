from __future__ import annotations

from _common import build_parser, load_config, print_config, release_placeholder, validate_manifest


def main() -> None:
    parser = build_parser("Run SHIELD inference on an NC-MRI case manifest.")
    args = parser.parse_args()
    cfg = load_config(args.config)
    manifest = args.manifest or getattr(cfg, "manifest", None)
    cases = validate_manifest(manifest)
    print(f"Validated {cases} manifest case(s) for inference.")
    if args.dry_run:
        print_config(cfg)
        return
    release_placeholder("Inference")


if __name__ == "__main__":
    main()

