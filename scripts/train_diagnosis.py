from __future__ import annotations

from _common import build_parser, load_config, print_config, release_placeholder, validate_manifest


def main() -> None:
    parser = build_parser("Train the SHIELD lesion diagnosis and interpretability module.")
    args = parser.parse_args()
    cfg = load_config(args.config, args.manifest)
    cases = validate_manifest(cfg.data.manifest)
    print(f"Validated {cases} manifest case(s) for diagnosis.")
    if args.dry_run:
        print_config(cfg)
        return
    release_placeholder("Diagnosis training")


if __name__ == "__main__":
    main()

